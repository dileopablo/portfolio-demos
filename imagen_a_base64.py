import base64
import os

# carpeta donde están las imágenes
carpeta_imagenes = "imagenes"

# archivo de salida
archivo_salida = "imagenes_base64.txt"

with open(archivo_salida, "w", encoding="utf-8") as salida:

    for archivo in os.listdir(carpeta_imagenes):

        if archivo.lower().endswith((".jpg", ".jpeg", ".png")):

            ruta = os.path.join(carpeta_imagenes, archivo)

            with open(ruta, "rb") as img:
                encoded = base64.b64encode(img.read()).decode("utf-8")

            # detectar tipo de imagen
            if archivo.lower().endswith(".png"):
                tipo = "png"
            else:
                tipo = "jpeg"

            # usar nombre del archivo como alt
            alt_text = os.path.splitext(archivo)[0].replace("_", " ")

            html = f'<img src="data:image/{tipo};base64,{encoded}" alt="{alt_text}" style="width:100%;height:140px;object-fit:cover;">\n\n'

            salida.write(html)

print("✅ Conversión terminada")
print(f"📄 HTML guardado en: {archivo_salida}")