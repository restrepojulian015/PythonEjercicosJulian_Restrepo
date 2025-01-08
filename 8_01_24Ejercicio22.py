#DICCIONARIO
repisa = ['Peluche', 'Libro', 'celular', 'lampara']
#OBJETO QUE ME PERMITE GUARDAR LOS ITERABLES DE ITER QUE OBTIENE DE REOISA
objetos = iter(repisa)

#RECORRE EL OBJETO OBJETO
for i in repisa:
    print(next(objetos))

# Ejemplo 2
mi_cadena = "Casa"
mi_iterable = iter(mi_cadena)


print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))


# Imprime
# C
# a
# s
# a