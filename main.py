from man_alum import Manejador_alum
from man_mat import Manejador_mat
if __name__=='__main__':
    m=Manejador_mat()
    a=Manejador_alum()
    a.agregar()
    m.carga()
    print(f'{a}')
    print('----Menu----\n1.Promedio con/sin aplazo\n2.Promocionales aprobados\n3.Alumnos\n')
    i=int(input('Ingrese opción, cualquier numero diferente para terminar:'))
    while i==1 or i==2 or i==3:
        match i:
            case 1:
                dni=int(input('\nIngrese dni:'))
                m.prom(dni)
            case 2:
                mat=input('\nIngrese materia:')
                m.busca(mat,a)
            case 3:
                a.listord()
        print('----Menu----\n1.Promedio con/sin aplazo\n2.Promocionales aprobados\n3.Alumnos\n')
        i=int(input('Ingrese opción, cualquier numero diferente para terminar:'))