## INTEGRANTES:
#     Quispe Taboada Daniel
#     Mamani Acha Alvin Jairo
#     Mamani Alarcon Anabel
#     Romero Orias Aurora
#     Terrazas Paco Shirley Guadalupe
#     Vidaurre Mejia Christian Paul

## Caso de nuestro agente:
#  Parcialmente observable
#  Agente individual
#  Entorno estocastico
#  Secuencial
#  Semidinamico
#  Discreto

import random as rd
import time

muro = "#"
espacio = " "
agente = "*"
espacioRecorrido = "·"
pelota = 'o'


def generar_Mapa(cc, ff):
    laberinto1 = []
    for i in range(0, ff):
        fila_laberinto = []
        for j in range(0, cc):
            fila_laberinto.append(muro)
        laberinto1.append(fila_laberinto)
    i_actual = rd.randrange(ff)
    j_actual = rd.randrange(cc)
    laberinto1[i_actual][j_actual] = espacio
    n_EG = 1
    while n_EG < n_Espacio:
        direccion = rd.randrange(4)
        if direccion == 0 and i_actual > 0:
            i_actual -= 1
        elif direccion == 1 and i_actual < ff - 1:
            i_actual += 1
        elif direccion == 2 and j_actual > 0:
            j_actual -= 1
        else:
            if j_actual < cc - 1:
                j_actual += 1
        if laberinto1[i_actual][j_actual] == muro:
            laberinto1[i_actual][j_actual] = espacio
            n_EG += 1
    n_p = 0
    while n_p < n_Pelota:
        ii = rd.randrange(ff)
        jj = rd.randrange(cc)
        if laberinto1[ii][jj] == espacio:
            laberinto1[ii][jj] = pelota
            n_p += 1
    return laberinto1


def imprimir(l_i):
    for line in l_i:
        print(" ".join(map(str, line)))


def Agente(lab_ag, ff, cc, n_P):
    inicio = time.time()
    n = 0
    intento = 1
    i = rd.randrange(f)
    j = rd.randrange(c)
    while lab_ag[i][j] != espacio:
        i = rd.randrange(f)
        j = rd.randrange(c)
    lab_ag[i][j] = agente
    i_anterior = i
    j_anterior = j
    print(" Intento " + str(intento))
    imprimir(lab_ag)
    dir = ''
    while n < n_P:
        intento += 1
        direccion = rd.randrange(4)
        if direccion == 0 and i > 0:
            dir = 'Arriba'
            i -= 1
        elif direccion == 1 and i < ff - 1:
            dir = 'Abajo'
            i += 1
        elif direccion == 2 and j > 0:
            dir = 'Izquierda'
            j -= 1
        elif direccion == 3 and j < cc - 1:
            dir = 'Derecha'
            j += 1
        else:
            dir = ''
        print("\n Intento " + str(intento))
        if (
            lab_ag[i][j] != muro
            and lab_ag[i][j] != agente
        ):
            if lab_ag[i][j] == pelota:
                n += 1
                print("  Se agarro la pelota Nro. "+str(n))
            lab_ag[i_anterior][j_anterior] = espacioRecorrido
            i_anterior = i
            j_anterior = j
            lab_ag[i][j] = agente
        else:
            if dir == 'Arriba':
                i += 1
            elif dir == 'Abajo':
                i -= 1
            elif dir == 'Izquierda':
                j += 1
            elif dir == 'Derecha':
                j -= 1
        imprimir(lab_ag)
        if n == n_P:
            final = time.time()
            print("El tiempo transcurrido es " + str(final-inicio))
            print("Se termino")


print("LABERINTO\n Laboratorio 2 de SIS420")
f = int(input("Introduzca la cantidad de filas del laberinto: "))
c = int(input("Introduzca la cantidad de columnas del laberinto: "))
n_Pelota = int(input("Introduzca la cantidad de pelotas del laberinto: "))
n_Pared = int(input("Introduzca la cantidad de muros del laberinto: "))
n_Espacio = (c * f) - n_Pared

laberinto_m = generar_Mapa(c, f)
imprimir(laberinto_m)
Agente(laberinto_m, f, c, n_Pelota)
