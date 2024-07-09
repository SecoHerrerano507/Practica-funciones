# main.py

from AnalizadorDeTextos import contar_palabras, reemplazar_palabra

# Ejemplos de uso de las funciones de análisis de texto

# Contar palabras
texto = "Buenos dias, Bryan"
print(f"Cantidad de palabras: {contar_palabras(texto)}")


# Reemplazar palabra
texto_modificado = reemplazar_palabra(texto, "Bryan", "Bryan Castillo")
print(f"Texto modificado: {texto_modificado}")
