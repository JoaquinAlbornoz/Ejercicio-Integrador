class Materia:
    def __init__(self,dni,nom,fecha,nota,ap):
        self.__dni=dni
        self.__nombre=nom
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=ap
    def __eq__(self,n):
        return self.__dni==n
    def __ge__(self,n):
        return self.__nota>=n
    def getnota(self):
        return self.__nota
    def getnombre(self):
        return self.__nombre
    def getap(self):
        return self.__aprobacion
    def getdni(self):
        return self.__dni
    def getfecha(self):
        return self.__fecha