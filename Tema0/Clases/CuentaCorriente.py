class CuentaCorriente():
    __DNI = ""
    __nombre = ""
    __saldo = 0

    def  __init__(self, DNI, saldo):
        self.__DNI = DNI
        self.__saldo = saldo
    
    def __init__(self, DNI, nombre, saldo):
        self.__DNI = DNI
        self.__nombre = nombre
        self.__saldo = saldo
    
    def __str__(self):
        return(self.__DNI + ": " + self.__nombre + " - " + str(self.__saldo))
    
    def __eq__(self, other):
        if isinstance(other, CuentaCorriente):
            return self.__DNI == other.__DNI
    
    def __lt__(self,other):
        if isinstance(other, CuentaCorriente):
            return self.__saldo < other.__saldo
    
    def sacarDinero(self, dinero):
        res = ""
        if(self.__saldo < dinero):
            res = "No hay suficientes fondos en la cuenta."
        else:
            self.__saldo -= dinero
            res = "Dinero sacado correctamente"
        return res
    
    def ingresarDinero(self, dinero):
        self.__saldo += dinero
        return "Saldo ingresado correctamente"
    

    
