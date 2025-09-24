"""Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120."""
num = int(input("Introduzca el numero del cual quiere calcular el factorial: "))
factorial = 1
for i in range(2, num + 1):
    factorial *= i
print(factorial)