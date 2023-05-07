import numpy as np
from alum import Alumno
import csv

class Manejador_alum:
    __incremento=5
    def __init__(self,dimension=10):
        self.__alumnos=np.empty(dimension,dtype=Alumno,)
        self.__dimension=dimension
        self.__cant=0
    def __str__(self):
        s=''
        for i in range(self.__cant):
            s=s+str(i)+str(self.__alumnos[i])+'\n'
        return s
    def agregar(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Ejercicio Integrador\\alumnos.csv','r') as archi:
            reader=csv.reader(archi,delimiter=';')
            for f in reader:
                if self.__cant==self.__dimension:
                    self.__dimension+=self.__incremento
                    self.__alumnos.resize(self.__dimension)
                a=Alumno(int(f[0]),f[1],f[2],f[3],int(f[4]))
                self.__alumnos[self.__cant]= a
                self.__cant+=1
    def buscarnombre(self,dni):
        i=0
        while i<self.__cant and self.__alumnos[i]!=dni:
            i+=1
        if i>=self.__cant:
            r='ERROR'
        else:
            r=self.__alumnos[i].getnom()
        return r
    def buscaranio(self,dni):
        i=0
        while i<self.__cant and self.__alumnos[i]!=dni:
            i+=1
        if i>=self.__cant:
            r='ERROR'
        else:
            r=self.__alumnos[i].getanio()
        return r
    def listord(self):
        l=[]
        for i in range(self.__cant):
            l.append(self.__alumnos[i])
        l.sort()
        for j in range(len(l)):
            print(l[j])
    