#Datos Personales:
nombre_completo="Mamani Acha Alvin Jairo"
carrera="Ing. de Sistemas"
cu="35-4846"
edad="21"
lugar_de_nacimineto="Sucre,Oropeza,Chuquisaca"

#Mostrar Datos Personales:
def mostrar_datos(nombre,carrera,cu,edad,lugar):
    print ("Nombre Completo: "+nombre)
    print ("Edad: "+edad)
    print ("Carrera: "+carrera)
    print ("CU: "+cu)
    print ("Lugar de Nacimineto: "+lugar)

#Ejecucion:
salida=0
while salida==0:
    print()
    print("             MI BIOGRAFIA     ")
    mostrar_datos(nombre_completo, carrera, cu, edad, lugar_de_nacimineto)
    datocorrecto=0
    while datocorrecto == 0:
        print()
        print("Menu:")
        print("Volver a Imprimir: 1")
        print("Salir: 2")
        opcion= int(input ("Introducir la operacion que desea realizar:"))
        if opcion == 1:
            datocorrecto=1
        if opcion == 2:
            salida=1
            datocorrecto=1
        print ()
        
   
print("Gracias!...")
