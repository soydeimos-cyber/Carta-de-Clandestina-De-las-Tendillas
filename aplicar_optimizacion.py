import os
import shutil

dir_origen = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/photos_optimizadas"
dir_destino = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/photos"

# Eliminar carpeta original y reemplazarla por la optimizada
if os.path.exists(dir_destino):
    shutil.rmtree(dir_destino)

os.rename(dir_origen, dir_destino)

# Note: The JS files referenced .png files, so we should update data.js to point to .jpg files.
data_path = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/data.js"
with open(data_path, "r", encoding="utf-8") as f:
    text = f.read()

# Super simple replace .png -> .jpg for "foto" property values
text = text.replace('.png"', '.jpg"').replace('.jpeg"', '.jpg"')

with open(data_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Imágenes optimizadas reemplazadas y referencias en data.js actualizadas a .jpg")
