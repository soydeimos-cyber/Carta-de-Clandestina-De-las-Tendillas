import os
from PIL import Image

def comprimir_imagenes(directorio_origen, directorio_destino, ancho_maximo=800, calidad=75):
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    for nombre_archivo in os.listdir(directorio_origen):
        ruta_origen = os.path.join(directorio_origen, nombre_archivo)
        
        # Ignorar directorios y procesar solo archivos que parezcan imágenes
        if os.path.isfile(ruta_origen) and nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                img = Image.open(ruta_origen)
                # Convertir RGBA a RGB si se va a guardar como JPEG
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    
                ancho_original, alto_original = img.size
                
                # Calcular nuevo tamaño manteniendo la proporción
                if ancho_original > ancho_maximo:
                    proporcion = ancho_maximo / float(ancho_original)
                    nuevo_alto = int((float(alto_original) * float(proporcion)))
                    img = img.resize((ancho_maximo, nuevo_alto), Image.Resampling.LANCZOS)
                
                # Guardar en destino (forzando formato JPEG para máxima compresión, o usar el formato original)
                # Para mayor reducción, vamos a guardar como .jpg incluso los originales .png
                nombre_base = os.path.splitext(nombre_archivo)[0]
                ruta_destino = os.path.join(directorio_destino, f"{nombre_base}.jpg")
                
                img.save(ruta_destino, 'JPEG', quality=calidad, optimize=True)
                print(f"Comprimida: {nombre_archivo} -> {nombre_base}.jpg")
                
            except Exception as e:
                print(f"Error procesando {nombre_archivo}: {e}")

if __name__ == "__main__":
    dir_origen = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/photos"
    dir_destino = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/photos_optimizadas"
    print("Iniciando compresión de imágenes...")
    comprimir_imagenes(dir_origen, dir_destino)
    print("¡Proceso completado!")
