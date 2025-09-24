import random
"""Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. 
El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1)."""
numRand = random.randint(1,100)
print(numRand)
numUsuario = int(input("Introduzca su intento"))
while(numUsuario != numRand and numUsuario != -1):
    if (numUsuario < numRand):
        print("El numero a acertar es mayor")
    else:
        print("El numero a acertar es menor")
    numUsuario = int(input("Introduzca su intento"))
if (numRand == numUsuario):
    print("Ole, acertaste")
else:
    print("Te has rendido :(")   