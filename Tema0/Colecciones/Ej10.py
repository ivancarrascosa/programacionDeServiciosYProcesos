"""
Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
conjunto 1:
e
i
k
m
p
q
r
s
t
u
v
conjunto 2: 
p
v
i
u
m
t
e
r
k
q
s

El programa debe pedir una frase al usuario y debe mostrar la frase encriptada.
Para ello, cada vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.
"""
encriptacion = {
    "e":"p",
    "i":"v",
    "k":"i",
    "m":"u",
    "p":"m",
    "q":"t",
    "r":"e",
    "s":"r",
    "t":"k",
    "u":"q",
    "v":"s"
    }

def encriptar():
    frase = input("Introduzca una frase para encriptar: ").lower()
    fraseEncriptada = ""
    for i in frase:
        if (encriptacion.get(i) != None):
            fraseEncriptada += encriptacion[i]
        else: 
            fraseEncriptada += i
    print(fraseEncriptada)

encriptar()