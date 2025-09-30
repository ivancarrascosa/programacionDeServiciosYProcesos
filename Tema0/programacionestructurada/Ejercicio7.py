##Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
num = int(input("Introduzca un numero para saber si es primo: "))
primo = True
divisor = 2
if(num < 1):
    print("El número no es primo")
else:
    while(primo and divisor <= num**0.5):
        if(num % divisor == 0):
            primo = False
        divisor += 1
if(primo):
    print("El número es primo.")
else:
    print("El número no es primo.")