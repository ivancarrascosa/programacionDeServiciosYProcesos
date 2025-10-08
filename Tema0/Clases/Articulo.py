class Articulo:

    IVA = 21

    def __init__(self, nombre, precio, cuantos_quedan):
        self.__nombre = nombre
        self.__precio = precio
        self.__cuantos_quedan = cuantos_quedan

    def getPVP(self):
        return self.__precio - self.__precio * Articulo.IVA / 100
    
    def getPVPDescuento(self, descuento):
        return getPVP(self.__precio * descuento /100)
    
    def vender(self, cantidad):
        posible = False
        if (self.__cuantos_quedan >= cantidad):
            self.__cuantos_quedan -= cantidad
        return posible
    
    def almacenar(self, cantidad):
        self.__cuantos_quedan += cantidad

    def __str__(self):
        return self.__nombre, self.__precio, '€', self.__cuantos_quedan, 'en stock.'
    
    def __eq__(self, other):
        if (isinstance(other, Articulo)):
            return self.__nombre == other.__nombre
    
    def __lt__(self, other):
        if (isinstance(other, Articulo)):
            return self.__nombre < other.__nombre