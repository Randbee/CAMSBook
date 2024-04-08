import nbformat
import os
import shutil
import re

# Función para obtener los nombres de los archivos de imagen de un notebook
def obtener_nombres_recursos(notebook):
    nombres_recursos = set()
    for cell in notebook.cells:
        if cell.cell_type == 'markdown':
            source = cell['source']
            # Buscar nombres de archivos de imagen y SVG en el markdown
            nombres_recursos.update(re.findall(r'!\[.*?\]\((.*?)\)', source))
    return nombres_recursos

# Directorio que contiene los notebooks y las imágenes
directorio_principal = '.'

# Directorio de salida para los notebooks clasificados
directorio_salida = '../notebooks'

# Crear directorio de salida si no existe
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Leer los notebooks y clasificarlos
for notebook_file in os.listdir(directorio_principal):
    if notebook_file.endswith('.ipynb'):
        nombre_notebook = os.path.splitext(notebook_file)[0]
        # Leer el notebook
        with open(os.path.join(directorio_principal, notebook_file), 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        # Obtener los nombres de los archivos de imagen y SVG
        nombres_recursos = obtener_nombres_recursos(notebook)
        # Crear una carpeta para el notebook
        carpeta_notebook = os.path.join(directorio_salida, nombre_notebook)
        if not os.path.exists(carpeta_notebook):
            os.makedirs(carpeta_notebook)
        carpeta_img = os.path.join(carpeta_notebook, 'img')
        if not os.path.exists(carpeta_img):
            os.makedirs(carpeta_img)
        # Mover el notebook al directorio de salida
        shutil.copy(os.path.join(directorio_principal, notebook_file), carpeta_notebook)
        print("Ruta actual:", os.getcwd())
        # Copiar los recursos al directorio del notebook
        for recurso in nombres_recursos:
            # Extraer el nombre del archivo de la ruta completa
            nombre_recurso = os.path.basename(recurso)
            ruta_recurso = os.path.join(*recurso.split('/'))
            # Copiar el recurso al directorio del notebook
            if os.path.exists(ruta_recurso):
                shutil.copy(ruta_recurso, carpeta_img)
                print("Recurso copiado: ", ruta_recurso)
            else:
                print(f'El recurso {ruta_recurso} no se encontró en el directorio de recursos.')

print("Proceso completado.")
