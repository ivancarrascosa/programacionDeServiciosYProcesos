"""
Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.
"""
def contadorPalabras(texto):
    diccionario = {}
    for i in texto.split(" "):
        if (diccionario.get(i) != None):
            diccionario[i] = diccionario[i] + 1
        else:
            diccionario[i] = 1
    return diccionario

print(contadorPalabras("Hola quiero saber como estas espero que estas bien Hola"))