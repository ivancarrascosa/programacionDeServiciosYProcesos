"""
Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 
"""
import random
print([random.randint(1,100) for x in range(10)])