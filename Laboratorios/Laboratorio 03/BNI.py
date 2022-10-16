## Integrangtes: Mamani Acha Alvin Jairo.
#                Quispe Taboada Daniel.
#  Laboratorio 03 
# 1. Implementamos la funcion de nodos_hijos, para poder 
# ver los estados que este podria llegar a tener.
# 2. -La Pc de Daniel Soporta hasta 7 digitos con una espera aproximada 
# de 20 segundos de busqueda.
#    -La Pc de Jairo soporta hasta 6 digitos con una respuesta rapida; con
# 7 digitos tarda alrededor de 2 min para solucionarlo.
# 3. Para poder usar una pila en vez de una cola, en la parte donde 
# se saca a un nodo de la lista frontera, se pone pop(0) para una lista 
# FIFO (primero en entrar, primero en salir) y pop() para una lista 
# LIFO ( ultimo en entrar, primero en salir)


import time
from nodo import *


def Busqueda(estado_inicio, estado_solucion, Tipo):
    if Tipo == 1:
        print('LIFO')
    elif Tipo == 2:
        print('FIFO')
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)

    while resuelto == False and len(nodos_frontera) != 0:
        if Tipo == 1:  # 1 => LIFO
            nodo_actual = nodos_frontera.pop()
        elif Tipo == 2:  # 2 => FIFO
            nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            lista_hijos = nodos_hijos(nodo_actual)
            for hijo in lista_hijos:
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)


def nodos_hijos(nodo):
    hijos = []
    n = len(nodo.get_datos())
    i = 0
    while i < n-1:
        hijo_datos = nodo.get_datos().copy()
        temp = hijo_datos[i]
        hijo_datos[i] = hijo_datos[i+1]
        hijo_datos[i+1] = temp
        hijo = Nodo(hijo_datos)
        nodo.set_hijo(hijo)
        hijos.append(hijo)
        i += 1
    return hijos


if __name__ == "__main__":
    estado_inicial = [7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7]
    inicio = time.time()
    nodo_solucion = Busqueda(estado_inicial, solucion, 1) #LIFO
    #nodo_solucion = Busqueda(estado_inicial, solucion, 2)  # FIFO
    fin = time.time()
    print('Tiempo de ejecucion: ', fin - inicio, 'seg.')
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print('\nMovimientos:')
    for i in resultado:
        print(i)
