'''
Un diccionario es una colección de elementos, donde cada uno consta
de una llave y un valor son dinámicos son indexados
pueden ser anidados
'''

diccionario = {
    "nombre": "Peter",
    "edad": 19,
    "esEstudainte": True,
    "Notas": {
        "nota1": 51,
        "nota2": 4,
        "nota2": 3.5,
    } 
}
#Otra Forma usando la función
#dict()
diccionario2 = dict(
    [
        ("nombre", "Jhon"),
        ("Edad", 28),
        ("esEstudiante", False)
    ]
)
#Segunda forma

diccionario3 = dict(
    nombre = "Jhon",
    edad = 28,
    esEStudiante = False
)
print(diccionario3)

#Acceder a un elemento

print(diccionario3["nombre"])
print(diccionario3.get("nombre"))

#Modificar un valor

diccionario3["nombre"] = "Michael"
print(diccionario3["nombre"])


#Iterar diccionarios 

for llave in diccionario:
    print(llave)
    print(diccionario[llave])


#obtener los llaves y valores en el diccionario
for llave, valor in diccionario.items():
    print(llave, valor)

print(diccionario.items())


#Metodods y funciones de los diccionarios 

#obtener el valor de una llave

print(diccionario2.get("hobby","No se ha encontrado"))

#Limpiar o vaciar el diccionario

diccionario3.clear()
print(diccionario3)

#Devolver una lista con todas las llaves del diccionario.
print(diccionario2.keys())


#Devolver una lista con todos los valores del diccionario
print(diccionario2.values())

#Elimina un elemento del diccionario
# Elimina elemento y devulve el valor

print(diccionario2.pop("Edad"))
print(diccionario2)

#Para evitar un error, se pasa un segundo elemento parametro con un valor por defecto
print(diccionario2.pop("direccion","no se ha encontrado"))

#Elimina aleatoriamente un elemento en el diccionario y lo devulve

print(diccionario2.popitem())

print(diccionario2)

'''
Actualizar un diccionario a partir de otro existente.
Actualizar las llavces comunes y agrega las del segundo diccionario que no estén en el primero
'''
diccionario2.update(diccionario2)
print(diccionario2)