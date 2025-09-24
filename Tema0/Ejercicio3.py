"""Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. Cuando el usuario no quiera insertar más números,
 introducirá un número negativo y el algoritmo, antes de acabar, mostrará la suma de los números positivos introducidos por el usuario."""
num = int(input("Introduzca un número para sumar"))
sum = 0
while num > 0:
    sum += num
    num = int(input("Introduzca un número para sumar"))
print(sum)