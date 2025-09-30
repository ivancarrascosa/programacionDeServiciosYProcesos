def calculadora(num1, num2, operacion):
    if operacion == 1:
        res = num1 + num2
    elif operacion == 2: 
        res = num1 - num2
    elif operacion == 3:
        res = num1 * num2
    elif operacion == 4:
        res = float(num1)/float(num2)
    else:
        res = "error"
    return res

print(calculadora(4,3,1))