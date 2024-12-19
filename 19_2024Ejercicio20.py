'''
Conjunto de datos parecidos a listas. pero a diferencia de las
'''
conjunto = set([1,8,15,5,8,9,"a","v","2a"])
'''
Los elementos del conjunto deben ser inmutables, por lo que no se puede asignar listas ni diccionarios.
'''

#lista = ["Perro","Gato"]
#onjunto = (set(["Conejo", "Ardilla", lista]))

'''
Recorrer los elementos de un conjunto
'''

conjunto1 = set(["a","b","c","d"])
for elemento in conjunto1:
    print(elemento)

#Contar los elementos en un conjunto

print(len(conjunto1))

print("b" in conjunto1)

#Unión de conjuntos

conjunto2 = set(["e","f","g"])
print(conjunto1.union(conjunto2))

conjunto2.add("h")
print(conjunto2)

conjunto2.remove("h")
print(conjunto2)

conjunto2.discard("h")
conjunto2.discard("f")
print(conjunto2)

conjunto2.pop()
print(conjunto2)

conjunto2.clear()
print(conjunto2)