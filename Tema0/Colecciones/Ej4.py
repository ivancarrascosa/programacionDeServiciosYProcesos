"""
Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.
"""
print(sorted([float(input("Introduzca un numero real")) for i in range(10)]))
