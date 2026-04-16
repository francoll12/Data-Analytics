matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
# En ciudades, cambia “Cancún” por “Monterrey”
# En las coordenadas, cambia el valor de “latitud” por 9.9355431


print(matriz[1][0])
matriz[1][0] = 6
print(matriz[1][0])

print(cantantes[0]['nombre'])
cantantes[0]['nombre'] = "Enrique Martin Morales"
print(cantantes[0]['nombre'])

print(ciudades['México'][2])
ciudades['México'][2] = "Monterrey"
print(ciudades['México'][2])

print(coordenadas[0]['latitud'])
coordenadas[0]['latitud'] = 9.9355431
print(coordenadas[0]['latitud'])



#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios 
#y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente
def iterarDiccionario(lista):
    for i in range(len(lista)):
        print(f"nombre - {lista[i]['nombre']}, pais - {lista[i]['pais']}")
        
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)
#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)


#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y 
#una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario 
#que se encuentra en la lista. 
#Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:

def iterarDiccionario2(llave, lista):
    for i in range(len(lista)):
        print(lista[i][llave])
        
iterarDiccionario2("pais", cantantes)

# Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. 
# La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto 
# los valores de la lista para esa clave. Por ejemplo:
def imprimirInformacion(diccionario):
    for llave in diccionario:
        print(f"{len(diccionario[llave])} {llave.upper()}")
        for i in range(len(diccionario[llave])):
            print(diccionario[llave][i])    

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)
