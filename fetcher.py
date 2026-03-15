import os
import shutil

# IDs and actual filenames found in NotebookLM
images = [
    ("70b9edbb-4eba-4ad6-8462-0cdb0666a954", "Albondigas de Ciervo.png"),
    ("25ec3795-8662-4743-91f4-b9180d5acf7f", "Alcachofas, yema, Boletus.png"),
    ("a371defa-6fce-4baf-b5b6-737d21300c4e", "Arroz de Changurro.png"),
    ("b2e4a9bb-6351-471b-af16-9628f79a9faf", "Bacalao en Témpura.png"),
    ("aee56ae6-cba4-4dfd-a1f4-cc0765eae8a4", "Callos.png"),
    ("11aa97ad-1365-4fc5-bd1e-d35571c96991", "Canelon de morteruelo.png"),
    ("080001b7-5b9e-4be5-a6e8-288c5e58b583", "Carrillada Atún.jpeg"),
    ("76b628b2-b5ba-4e18-83ae-99616c46a858", "Cochinillo.png"),
    ("ce2780db-5b59-442c-b595-655d9706c3b2", "Croqueta de Jamón Ibérico.png"),
    ("8650ee93-d995-45dc-a61e-35f9fbd47e5d", "Cúpula Chocolate.jpeg"),
    ("2b79257e-0c6c-4c4d-ad47-84120abe0681", "Ensaladilla.png"),
    ("6119899b-c5ee-44ad-a5fb-666c18c92d4f", "Gilda.png"),
    ("3312d24d-2e46-4e1b-b98b-7839d20d0fdb", "Lomo Ciervo.png"),
    ("ef8746b6-425a-4193-913b-00ccc2700523", "Pochas con Perdiz.png"),
    ("4ce6b727-350d-4987-b1f5-b96834cc7adb", "Presa Iberica.png"),
    ("bc4d6a1b-7abd-4f8d-8b1d-9e9b51f77944", "Pulpo.png"),
    ("ade6d5f0-0a39-4573-aa1a-127eefdfab49", "Ruibarbo.jpeg"),
    ("1d0cd211-2990-4298-8f07-06d27f6a4377", "Steak Tartar.png"),
    ("c1d286e1-d411-436d-8385-226635d2b2be", "Tarta queso.png"),
    ("e173896c-b363-46ed-8e56-950f4619eb76", "Torrija de pan Brioche.png"),
    ("bcbf000f-5a15-4a95-a7fc-de4d79e660f3", "anchoa 00.png"),
    ("7b2c4205-7e55-4f4a-b8c7-39ad3224594f", "carrillada jabali.png"),
    ("f11cdc7f-381e-41f0-8c13-81fad84327b0", "crujiente de bacalao.png"),
    ("f2df3921-089c-4f80-a8e6-76b8993e090c", "ensalala de perdiz.png")
]

# Write a quick list we can use with MCP to fetch them
import sys
# Just list to console so we can get them with tool
for id, name in images:
    print(f"ID:{id}|NAME:{name}")
