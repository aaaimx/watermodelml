import PyPDF3
from PIL import Image

# Abre el archivo PDF y crea un objeto de la clase PdfFileReader
with open('1986.pdf', 'rb') as archivo_pdf:
    lector_pdf = PyPDF3.PdfFileReader(archivo_pdf)

# Obtén el número de páginas del archivo PDF
num_paginas = lector_pdf.getNumPages()

# Itera sobre todas las páginas del archivo PDF y extrae las tablas utilizando la biblioteca PyPDF2
for pagina in range(num_paginas):
    pagina_actual = lector_pdf.getPage(pagina)
    contenido_pagina = pagina_actual.extractText()
    # Procesa los datos de la tabla y crea una imagen de la tabla
    imagen_tabla = Image.frombytes('RGB', (anchura, altura), imagen_binaria)
    # Guarda la imagen de la tabla
    imagen_tabla.save(f'pagina_{pagina + 1}_tabla.png')
