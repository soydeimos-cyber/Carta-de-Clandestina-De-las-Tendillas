import json
import os

data_path = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/data.js"
photos_path = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/photos"

with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

prefix, js_data = text.split("window.menuData = ", 1)
js_data = js_data.strip().rstrip(";")

try:
    data = json.loads(js_data)
except Exception as e:
    print("Error parsing JSON:", e)
    import sys
    sys.exit(1)

# List of photos in the directory
photo_files = os.listdir(photos_path)

# Map names to expected files
mapping = {
    "SURTIDO DE PAN TRADICIONAL": "Cesto de pan.jpg",
    "BARRITA DE PAN SIN GLUTEN": "Cesto de pan.jpg",
    "BERENJENA ASADA AL MISO, REQUESÓN Y TRUCHA MARINADA": "berengena.jpg"
}

updated_count = 0
for item in data:
    nombre = item["nombre"]
    if nombre in mapping:
        img_name = mapping[nombre]
        if img_name in photo_files:
            item["foto"] = img_name
            updated_count += 1
            print(f"Assigned {img_name} to {nombre}")

if updated_count > 0:
    updated_text = prefix + "window.menuData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(data_path, "w", encoding="utf-8") as f:
        f.write(updated_text)
    print("Updated data.js with new photos.")
else:
    print("No new photos assigned.")
