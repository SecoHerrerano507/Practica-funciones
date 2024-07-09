# Autor: Bryan Castillo
# Fecha" 08/07/2024
# Version: 3.12.3 64-bit

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def reemplazar_palabra(texto, palabra_a_reemplazar, nueva_palabra):
    return texto.replace(palabra_a_reemplazar, nueva_palabra)