import nbformat
import os
import re

# Función para actualizar las rutas de las imágenes en un notebook
def actualizar_rutas_imagenes(notebook):
    for cell in notebook.cells:
        if cell.cell_type == 'markdown':
            source = cell['source']
            # Buscar rutas de imágenes en el texto markdown
            imagenes = re.findall(r'!\[.*?\]\((.*?)\)', source)
            for ruta_imagen in imagenes:
                # Comprobar si la ruta es una URL
                if not es_url(ruta_imagen):
                    # Formatear la ruta de la imagen
                    nueva_ruta_imagen = './img/' + os.path.basename(ruta_imagen)
                    # Reemplazar la ruta de la imagen en el texto markdown
                    source = source.replace(ruta_imagen, nueva_ruta_imagen)

            cell['source'] = source

# Función para verificar si una cadena es una URL
def es_url(cadena):
    # Puedes mejorar esta verificación según tus necesidades
    return cadena.startswith('http://') or cadena.startswith('https://')

# Directorio que contiene los notebooks y las imágenes
directorio_principal = os.path.join('.') # Directorio de cada carpeta de notebook

# Leer los notebooks y actualizar las rutas de las imágenes
for notebook_folder in os.listdir(directorio_principal):
    if os.path.isdir(notebook_folder):
        for notebook_file in os.listdir(notebook_folder):
            if notebook_file.endswith('.ipynb'):
                # Leer el notebook
                with open(os.path.join(directorio_principal, notebook_folder, notebook_file), 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)
                # Actualizar las rutas de las imágenes
                actualizar_rutas_imagenes(notebook)
                # Guardar el notebook actualizado
                with open(os.path.join(directorio_principal, notebook_folder, notebook_file), 'w', encoding='utf-8') as f:
                    nbformat.write(notebook, f)
                print("Rutas de imágenes actualizadas en:", notebook_file)

print("Proceso completado.")
