class Libro():
    def __init__(self, titulo, autor, numeroDeEjemplares, ejemplaresPrestados):
        self.__titulo = titulo
        self.__autor = autor
        self.__numeroDeEjemplares = numeroDeEjemplares
        self.__ejemplaresPrestados = ejemplaresPrestados
    
    def prestamo(self):
        posible = False
        if (self.__numeroDeEjemplares > 0):
            self.__ejemplaresPrestados += 1
            self.__numeroDeEjemplares -= 1
            posible = True
        return posible
    
    def devolucion(self):
        posible = False
        if (self.__ejemplaresPrestados > 0):
            self.__ejemplaresPrestados -= 1
            self.__numeroDeEjemplares += 1
            posible = True
        return posible
    
    def __str__(self):
        return ('Titulo:',self.__titulo, 'Autor:', self.__autor, 'Numero de ejemplares:',self.__numeroDeEjemplares,'Ejemplares prestados:',self.__ejemplaresPrestados)
    
    def __eq__(self, other):
        if (isinstance(other, Libro)):
            return (self.__autor == other.__autor and self.__titulo == other.__titulo)
        
    def __lt__(self, other):
        if (isinstance(other, Libro)):
            return self.__autor < other.__autor
