class Animal:
    def __init__(self, nombre, numero_patas = 4):
        self.__nombre = nombre
        self.__numero_patas = numero_patas
    
    def habla(self):
        return ''
    
    def __str__(self):
        return f"Me llamo {self.__nombre}, tengo {self.__numero_patas} patas y sueno así: {self.habla()}"
    
class Gato(Animal):
    
    def habla(self):
        return 'Miau'
    
    def __str__(self):
        return 'Soy un gato. ' + super().__str__()

class Perro(Animal):
    
    def habla(self):
        return 'Guau'
    
    def __str__(self):
        return 'Soy un perro. ' + super().__str__()

if __name__ == "__main__":
    gato = Gato("Michi")
    perro = Perro("Firulais")

    print(gato)   # Soy un gato. Me llamo Michi, tengo 4 patas y sueno así: Miau
    print(perro)  # Soy un perro. Me llamo Firulais, tengo 4 patas y sueno así: Guau

    # Comprobar que el método habla funciona
    print(gato.habla())   # Miau
    print(perro.habla())  # Guau

    # Crear animal genérico (sin sonido)
    animal = Animal("Criatura", 2)
    print(animal)         # Me llamo Criatura, tengo 2 patas y sueno así: