import json

data_path = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/data.js"

with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

prefix, js_data = text.split("window.menuData = ", 1)
js_data = js_data.strip().rstrip(";")

data = json.loads(js_data)

for item in data:
    if "PAN" in item["nombre"]:
        if "precio por persona" not in item["descripcion"].lower():
            if item["descripcion"]:
                item["descripcion"] += " (Precio por persona)."
            else:
                item["descripcion"] = "Precio por persona."

updated_text = prefix + "window.menuData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(data_path, "w", encoding="utf-8") as f:
    f.write(updated_text)

print("Updated bread descriptions.")
