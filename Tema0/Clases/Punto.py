import math

class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return '(' + str(self.__x) + ',' + str(self.__y) + ')'
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y
    
    def desplaza(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distancia(self, other):
        if (isinstance(other, Punto)):
            return math.sqrt(math.pow(self.__x - other.__x, 2) + math.pow(self.__y - other.__y, 2))

if __name__ == "__main__":
    # Crear dos puntos
    p1 = Punto(0, 0)
    p2 = Punto(3, 4)

    # Imprimir puntos
    print("Punto 1:", p1)
    print("Punto 2:", p2)

    # Calcular distancia entre ellos (debería ser 5.0)
    print("Distancia entre p1 y p2:", p1.distancia(p2))

    # Desplazar p1 en (1, 1)
    p1.desplaza(1, 1)
    print("Punto 1 desplazado:", p1)

    # Cambiar coordenadas de p2 a (0,0)
    p2.setXY(0, 0)
    print("Punto 2 actualizado:", p2)

    # Nueva distancia
    print("Nueva distancia entre p1 y p2:", p1.distancia(p2))