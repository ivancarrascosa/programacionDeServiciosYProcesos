"""Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. Desde el método main() lee los dos números enteros,
 los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función."""

def printNumbers(num1, num2):
    if(num1 < num2):
        for i in range(num1 + 1, num2):
            print(i)
    else:
        for i in range(num2 + 1, num1):
            print(i)

def Main():
    num1 = int(input("introduzca el primer número: "))
    num2 = int(input("introduzca el segundo número: ")) 
    printNumbers(num1,num2)

Main()
