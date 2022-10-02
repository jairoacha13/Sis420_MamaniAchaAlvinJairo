#Ejercicios sacados del libro "How to code in python"

from pickle import TRUE


print("Ejemplos de Listas:")
print("1er Ejercicio: ")
animales_marinos=["shark","cuttlefish","squid","mantis shrimp","anemone"]
print(animales_marinos)
print()

print("2do Ejercicio: ")
print("Sammy es un "+ animales_marinos[0])
print()

print("3er Ejercicio: ")
animales_marinos=["shark","octopus","blobfish","mantis shrimp","anemone"]
oceanos=["Pacifico","Atlantico","Indico","Meridional","Artico"]
print(animales_marinos + oceanos)
print()

print("4to Ejercicio: ")
animales_marinos = animales_marinos+ ["yeti crab"]
print(animales_marinos)
print()

print("5to Ejercicio: ")
print(animales_marinos*2)
print(oceanos*3)
print()

print("6to Ejercicio: ")
animales_marinos=["shark","cuttlefish","squid","mantis shrimp","anemone"]
for x in range (1,4):
    animales_marinos += ["fish"]
    print (animales_marinos)
print()

print("7mo Ejercicio: ")
sharks=["shark"]
for x in range(1,4):
    sharks *= 2
    print(sharks)
print()

print("Ejemplos de Diccionarios:")
print("1er Ejercicio: ")
sammy = {'username':'sammy-shark','online':True,'seguidores':987}
print (sammy['username'])
print (sammy['online'])
print (sammy['seguidores'])
print()

print("2do Ejercicio: ")
sammy = {'username':'sammy-shark','online':True,'seguidores':987}
jesse = {'username':'Joctopus','online':False,'seguidores':720}

for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])
print()

print("3er Ejercicio: ")
for key,value in sammy.items():
    print(key, "is the key for the value", value)
print()

print("4to Ejercicio: ")
drew = {'username': 'squidly', 'online': True, 'seguidores': 305}
print(drew)
drew['seguidores']=405
print(drew)
print()



