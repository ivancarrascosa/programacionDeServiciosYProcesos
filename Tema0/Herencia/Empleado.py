class Empleado:
    def __init__(self, nombre):
        self.__nombre = nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Empleado {self.__nombre}"
    
class Operario(Empleado):
    
    def __str__(self):
        return super().__str__() + " -> Operario"
    
class Directivo(Empleado):
    
    def __str__(self):
        return super().__str__() + " -> Directivo"
    
class Oficial(Operario):
    
    def __str__(self):
        return super().__str__() + " -> Oficial"
    
class Tecnico(Operario):
    
    def __str__(self):
        return super().__str__() + " -> Tecnico"
    
e = Empleado("Juan")
o = Operario("Carlos")
d = Directivo("Ana")
of = Oficial("Luis")
t = Tecnico("Pedro")

print(e)   # Empleado Juan
print(o)   # Empleado Carlos -> Operario
print(d)   # Empleado Ana -> Directivo
print(of)  # Empleado Luis -> Operario -> Oficial
print(t)   # Empleado Pedro -> Operario -> Tecnico
