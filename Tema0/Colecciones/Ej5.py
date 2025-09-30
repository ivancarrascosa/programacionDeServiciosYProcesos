"""
Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene
con valores enteros aleatorios entre 1 y 10. Luego pedirá un valor N y mostrará cuántas veces aparece N. 
"""
import random
listaRandom = [random.randint(1,10) for x in range(100)]
numeroBuscar = int(input("Indique un numero del 1 al 10 para saber cuantas veces aparece."))
print(listaRandom.count(numeroBuscar))