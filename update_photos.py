import json
import os

data_path = "C:/Users/pcsag/.gemini/antigravity/scratch/menu_app/data.js"
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

mapping = {
    "CROQUETA DE LECHE DE OVEJA E IBÉRICO DE BELLOTA": "Croqueta.png",
    "CRUJIENTE DE BACALAO AL AJO ARRIERO": "crujiente de bacalao.png",
    "ANCHOA 00, NARANJA Y ALBAHACA": "anchoa 00.png",
    "LOMO DE SARDINA MARINADA EN BLANCO": "sardina.png",
    "ALBÓNDIGA DE CIERVO, TARTUFATA Y PARMENTIER DE ZANAHORIA": "Albondigas de Ciervo.png",
    "GILDA TRADICIONAL": "Gilda.png",
    "ALCACHOFAS SALTEADAS, CREMA DE BOLETUS Y YEMA CURADA CON FURIKAKE": "Alcachofas.png",
    "CANELÓN DE MORTERUELO (2 UNID), FOIE Y JUGO DE RATAFIA": "Canelon.png",
    "ENSALADILLA TRADICIONAL CON VENTRESCA DE ATÚN": "Ensaladilla.png",
    "BERENJENA ASADA AL MISO, REQUESÓN Y TRUCHA MARINADA": "placeholder.jpg",
    "ENSALADA DE PERDIZ, EMULSIÓN DE ESCABECHE, MENTA Y CEBOLLA": "ensalala de perdiz.png",
    "CALLOS TRADICIONALES": "Callos.png",
    "ALBÓNDIGAS DE CIERVO, TARTUFATA Y PARMENTIER DE ZANAHORIA": "Albondigas de Ciervo.png",
    "ARROZ MELOSO DE CHANGURRO, AMERICANA DE MORCILLA Y AZAFRÁN": "Arroz.png",
    "CARRILLERA DE ATÚN ROJO, APIO NABO Y TIRABEQUES": "Carrillada Atún.jpeg",
    "STEAK TARTAR DE WAGYU SOBRE TUETANO": "Steak Tartar.png",
    "PRESA IBÉRICA ADOBADA, JUGO DE CAFÉ, SETAS SHITAKE Y HUMMUS": "Presa Iberica.png",
    "COCHINILLO DESHUESADO A BAJA TEMPERATURA, SU JUGO Y TEXTURAS DE BERENJENA": "Cochinillo.png",
    "PULPO, MOJETE MANCHEGO Y PATATA A LAS HIERBAS": "Pulpo.png",
    "BACALAO EN TEMPURA DE TRISOL, TIZNAO Y EMULSIÓN DE CEBOLLINO": "Bacalao.png",
    "LOMO DE CIERVO, MOLE Y MILHOJAS DE QUESO MANCHEGO Y PATATA": "Lomo Ciervo.png",
    "CARRILLADA DE JABALÍ, CREMA DE CEBOLLA Y ALMENDRA": "carrillada jabali.png",
    "POCHAS ESTOFADAS CON PERDIZ": "Pochas con Perdiz.png",
    "RUIBARBO, HELADO DE ROSAS, TIERRA DE LECHE Y YOGURT": "Ruibarbo.jpeg",
    "TARTA DE QUESO MANCHEGO Y HELADO DE MIEL": "Tarta queso.png",
    "TORRIJA DE PAN BRIOCHE, TOFFE Y HELADO DE CAFÉ": "Torrija de pan Brioche.png",
    "CÚPULA DE CHOCOLATE, FRUTOS SECOS Y FRAMBUESA": "Cúpula Chocolate.jpeg"
}

for item in data:
    if item["nombre"] in mapping:
        item["foto"] = mapping[item["nombre"]]

updated_text = prefix + "window.menuData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open(data_path, "w", encoding="utf-8") as f:
    f.write(updated_text)

print("Updated data.js successfully.")
