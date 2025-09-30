"""
Realiza un programa que pida 8 números enteros y los almacene en una lista.
 A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.
"""
listaNumeros = [int(input("Introduzca un numero entero")) for i in range(8)]
for i in listaNumeros:
    if (i%2 == 1):
        print(str(i) + "    impar")
    else:
        print(str(i) + "    par")