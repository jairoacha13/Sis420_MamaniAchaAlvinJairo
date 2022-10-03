import random

#Pedir Datos:
numero_filas= int(input ("Introducir el numero de filas:"))
numero_columnas= int(input ("Introducir el numero de columnas:"))
numero_paredes= int(input ("Introducir el numero de paredes:"))
numero_espacios= (numero_filas*numero_columnas)-numero_paredes

#Crear el laberinto con pura paredes:
laberinto=[]
for i in range(0,numero_filas):
    laberinto.append(["#"]*(numero_columnas))

#Imprimir el laberinto:
def mostrar_laberinto():
    cont=0
    print()
    for fila in laberinto:
        print('[',end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        cont+=1
        print(']')
    print ()

#Colocar espacios libres:
numero_espacios_generados = 0
    #Creando tres puntos de inicio.Esto para que no todos los espacios se centren en un sector del laberinto.
while numero_espacios_generados<3:
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1
    #Completando los demas espacios a partir de los puntos de inicio creados anteriormente.
while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            numero_espacios_generados += 1

#Incluir un agente en un espacio libre:
colocada=0
while colocada==0:
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    if laberinto[ficha_fila][ficha_columnas] == ' ':
        laberinto[ficha_fila][ficha_columnas] = '$'
        colocada=1
#Mover al agente cinco cuadros seguidos:
movimiento=0
while movimiento < 5:
        direccion = random.randrange(4)
        if direccion == 0 and ficha_fila > 0:
            ficha_fila -= 1
        elif direccion == 1 and ficha_fila < numero_filas - 1:
            ficha_fila += 1
        elif direccion == 2 and ficha_columnas > 0:
            ficha_columnas -= 1
        else:
            if ficha_columnas < numero_columnas - 1:
                ficha_columnas += 1
            
        if laberinto[ficha_fila][ficha_columnas] == ' ':
            laberinto[ficha_fila][ficha_columnas] = '$'
            movimiento += 1

#Llamando a la funcion mostrar laberinto:
mostrar_laberinto()