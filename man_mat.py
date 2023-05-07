import csv
from mat import Materia
from man_alum import Manejador_alum
class Manejador_mat:
    def __init__(self):
        self.__listam=[]
    def carga(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Ejercicio Integrador\\materiasAprobadas.csv') as a:
            reader=csv.reader(a,delimiter=';')
            for f in reader:
                m=Materia(int(f[0]),f[1],f[2],int(f[3]),f[4])
                self.__listam.append(m)
    def prom(self,dni):
        a=0
        x=0
        j=0
        sa=0
        for i in range(len(self.__listam)):
            if self.__listam[i]==dni:
                x+=1
                if self.__listam[i]>=4:
                    sa+=self.__listam[i].getnota()
                    j+=1
                a+=self.__listam[i].getnota()
        print(f'\nPromedio sin aplazo:{sa/j} Promedio con aplzao:{a/x}\n')
    def busca(self,mat,m=Manejador_alum()):
        print('DNI\t\tApellido y Nombre\tFecha\tNota\tAño que cursa')
        for i in range(len(self.__listam)):
                if self.__listam[i].getnombre()==mat and self.__listam[i].getap()=='P' and self.__listam[i]>=7:
                    print(f'{self.__listam[i].getdni()}\t{m.buscarnombre(self.__listam[i].getdni())}\t\t{self.__listam[i].getfecha()}\t{self.__listam[i].getnota()}\t{m.buscaranio(self.__listam[i].getdni())}')

