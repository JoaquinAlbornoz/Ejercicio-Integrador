class Alumno:
    def __init__(self,dni,ap,nom,carr,anio):
        self.__dni=dni
        self.__apellido=ap
        self.__nombre=nom
        self.__carrera=carr
        self.__anio=anio
    def __str__(self):
        return f'{self.__dni} {self.__apellido} {self.__nombre} {self.__carrera} {self.__anio}'
    def __ne__(self,n):
        return self.__dni!=n
    def __gt__(self,n):
        if type(n)==type(self):
            if self.__anio==n.getanio():
                g = self.__apellido>n.getap()
            else:
                g = self.__anio>n.getanio() 
        else:
            if self.__anio==n:
                g = self.__apellido>n
            else:
                g = self.__anio>n
        return g
    def __lt__(self,n):
        if type(n)==type(self):
            if self.__anio==n.getanio():
                g = self.__apellido<n.getap()
            else:
                g = self.__anio<n.getanio() 
        else:
            if self.__anio==n:
                g = self.__apellido<n
            else:
                g = self.__anio<n
        return g
    def getdni(self):
        return self.__dni
    def getnom(self):
        return self.__apellido + self.__nombre
    def getanio(self):
        return self.__anio 
    def getap(self):
        return self.__apellido