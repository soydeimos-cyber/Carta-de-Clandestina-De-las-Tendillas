import json
import re

data_path = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/data.js"
input_path = "C:/Users/pcsag/.gemini/antigravity/brain/5f35435a-f488-4c38-8e4f-7d93fd15c1d2/.system_generated/steps/25/output.txt"

with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

prefix, js_data = text.split("window.menuData = ", 1)
js_data = js_data.strip().rstrip(";")

try:
    old_data = json.loads(js_data)
except Exception as e:
    print("Error parsing data.js:", e)
    import sys
    sys.exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    input_text = f.read()

try:
    notebook_output = json.loads(input_text)
    new_items_raw = json.loads(notebook_output.get("answer", "").replace("```json\n", "").replace("\n```", ""))
except Exception as e:
    print("Error parsing notebook output:", e)
    import sys
    sys.exit(1)

updated_data = []

# Keep a map of old items to preserve allergies, etc.
old_map = {item["nombre"].lower().strip(): item for item in old_data}

default_cat = "principal"
for item in new_items_raw:
    nombre = item["nombre"]
    nombre_key = nombre.lower().strip()
    
    desc_cleaned = re.sub(r'\s*\[\d+\]', '', item["descripcion"])
    
    if nombre_key in old_map:
        old_item = old_map[nombre_key]
        old_item["descripcion"] = desc_cleaned
        old_item["precio"] = item["precio"]
        updated_data.append(old_item)
    else:
        # New item
        new_item = {
            "nombre": nombre,
            "precio": item["precio"],
            "alergenos": [],
            "opciones_veganas_vegetarianas": False,
            "opciones_sin_gluten": False,
            "categoria": default_cat,
            "foto": "",
            "descripcion": desc_cleaned
        }
        updated_data.append(new_item)

updated_text = prefix + "window.menuData = " + json.dumps(updated_data, indent=2, ensure_ascii=False) + ";\n"

with open(data_path, "w", encoding="utf-8") as f:
    f.write(updated_text)

print("Updated data.js successfully.")
