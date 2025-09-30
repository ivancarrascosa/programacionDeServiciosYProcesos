"""
Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones
implementada como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número
de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.
"""
agenda = {"Pepe": 1, "Jose": 2}
def agregarContacto(nombre, telefono):
    agenda[nombre] = telefono

def eliminarContacto(nombre):
    if(agenda.get(nombre) != None):
        agenda.pop(nombre)
        print("Contacto borrado correctamente.")
    else: 
        print("No se ha encontrado este contacto.")

def buscarNumero(nombre):
    return(agenda.get(nombre, "Número no encontrado."))

def main():
    opc = int(input("Selecciona una opción del menú: \n1. Añadir contacto \n2. Eliminar contacto \n3. Buscar numero\n4. Salir\n"))
    while(opc != 4):
        if (opc == 1):
            nombre = input("Introduzca el nombre del contacto que quiere añadir: ")
            telefono = input("Introduzca el número de la persona: ")
            agregarContacto(nombre, telefono)
        elif(opc == 2):
            nombre = input("Introduzca el nombre del contacto que quiere eliminar: ")
            eliminarContacto(nombre)
        elif(opc == 3):
            nombre = input("Introduzca el contacto del cual quiere ver el número: ")
            print(buscarNumero(nombre))
        elif(opc == 4):
            print("Saliendo...")
        else:
            print("Introduzca una opción correcta.")
        opc = int(input("Selecciona una opción del menú: \n1. Añadir contacto \n2. Eliminar contacto \n3. Buscar numero\n4. Salir\n"))
main()