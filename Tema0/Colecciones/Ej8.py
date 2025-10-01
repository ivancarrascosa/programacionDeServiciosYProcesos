"""
Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres de los productos
y los valores son las cantidades vendidas. El programa debe permitir al usuario agregar nuevas ventas y calcular el total de 
ventas para un producto específico. Implementa un menú con ambas opciones.
"""
ventas = {}

def añadirVenta(producto, cantidad):
    if ventas.get(producto) != None:
        ventas[producto] = ventas[producto] + cantidad
    else:
        ventas[producto] = cantidad

def verVentas(producto):
    return(ventas.get(producto, "Producto no encontrado."))

def main(): 
    opc = int(input("Selecciona una opción del menú: \n1. Añadir venta \n2. Ver ventas de producto\n3. Salir\n"))
    while(opc != 3):
        if opc == 1:
            producto = input("Introduzca el producto que se ha vendido: ")
            cantidad = int(input("Introduzca la cantidad del producto vendido: "))
            añadirVenta(producto, cantidad)
            print("Ventas añadidas correctamente")
        elif opc == 2: 
            producto = input("Introduzca el nombre del producto del cual quiere ver las ventas: ")
            print(verVentas(producto))
        elif opc == 3:
            print("Saliendo...")
        else:
            print("Seleccione una opción correcta.")
        opc = int(input("Selecciona una opción del menú: \n1. Añadir venta \n2. Ver ventas de producto\n3. Salir\n"))

main()