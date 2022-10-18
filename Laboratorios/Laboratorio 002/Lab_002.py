#Nombre: Mamani Acha Alvin Jairo.
##
#-El codigo solo funciona con hasta 6 digitos en un tiempo aproximado
# de 2 seg.
#-La principal dificultad es que el codigo crea demasiados estados que
# son innecesarios para la solucion, una opcion para mejorar esto seria
# brindarle informacion de cuando va por un camino beneficioso, o por el
# otro lado si es un camino innecesario que ya no lo revise.

from nodo import * 
import time

def resolver_rompecabezas(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    
    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0) #FIFO - cola
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for i in range(len(estado_inicio)-1): 
                hijo_datos = nodo_actual.get_datos().copy()    
                temp = hijo_datos[i]
                hijo_datos[i] = hijo_datos[i+1]
                hijo_datos[i+1] = temp
                hijo = Nodo(hijo_datos)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)

if __name__ == "__main__":
    estado_inicial = [6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6]
    start = time.time()
    nodo_solucion = resolver_rompecabezas(estado_inicial, solucion)
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
    #print('\n',resultado)
    print('Movimientos : \n')
    for i in range(len(resultado)):
      print(resultado[i])