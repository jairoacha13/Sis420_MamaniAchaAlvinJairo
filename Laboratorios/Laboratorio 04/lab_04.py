## Alumno: Mamani Acha Alvin Jairo.
## Carrera: Ing. de Sistemas.
## CU: 35-4846.
##
## 1) El codigo tiene como capacidad limite 6 digitos, el problema con 7 
##    es que se crean demasiados nodos, y al ser los costos asignados de manera 
##    aleatorio hacen que el camino sea mas largo.
## 2) Una mejora para el codigo podria ser el de ya no asignar aleatoriamente los
##    costos, si no asignar de acuerdo a si el nodo esta mas cerca de la solucion, 
##    darle un valor mayor para que el codigo le de prioridad y lo revise primero;
##    esto ayudaria ha ampliar la capacidad del rompecabezas y resolverlo mas 
##    rapidamente.

import time
from nodo import *
from random import randint

def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodo_inicio.set_costo(randint(50,200)) # --> Añadiendo un costo al nodo inicio.
    nodos_frontera.append(nodo_inicio)

    while resuelto == False and len(nodos_frontera) != 0:
        ordenar(nodos_frontera) # --> Ordenar 'nodos_frontera' de mayor a menor.
            #print ('Ordenando:'+'****'*10)
            #imprimir(nodos_frontera) # --> Verificar que se este ordenando correctamente.
        nodo_actual = nodos_frontera.pop(0) #FIFO - cola
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for j in range(len(estado_inicio)-1): 
                hijo_datos = nodo_actual.get_datos().copy()    
                temp = hijo_datos[j]
                hijo_datos[j] = hijo_datos[j+1]
                hijo_datos[j+1] = temp
                hijo = Nodo(hijo_datos)
                hijo.set_costo(randint(50,200)) # --> Añadiendo un costo a los hijos.
                
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)

# Funcion para ordenar de mayor a menor los nodos que se encuentran en 'nodos_frontera'
def ordenar(frontera):
    n = len(frontera)
    for i in range(n-1):       
        for j in range(n-1-i): 
            if frontera[j].costo < frontera[j+1].costo:
                frontera[j].costo, frontera[j+1].costo = frontera[j+1].costo, frontera[j].costo

#def imprimir(f):
#    for i in range (len(f)):
#        print ('-', f[i].costo)

if __name__ == "__main__":
    estado_inicial = [6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6]
    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end =time.time()
    print('Tiempo de ejecucion : ',end-start, 'seg.','\n')
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print("*****"*10)
    #print('\n',resultado)
    print('Movimientos : \n')
    for i in range(len(resultado)):
      print(resultado[i])
