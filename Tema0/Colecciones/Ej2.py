"""
Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.
"""
listaNumeros = [float(input("Introduzca un numero real")) for i in range(10)]
minimo = listaNumeros[0]
maximo = listaNumeros[0]
for i in range(1,len(listaNumeros)):
    numActual = listaNumeros[i]
    if (numActual < minimo):
        minimo = numActual
    elif (numActual > maximo):
        maximo = numActual
print(minimo)
print(maximo)
print(min(listaNumeros))
print(max(listaNumeros))