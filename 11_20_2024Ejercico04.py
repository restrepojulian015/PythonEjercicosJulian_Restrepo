# Programa que me calcula el promedio ponderado a paritr de cuatro notas
n1 = int(input("Ingresa la primera nota parcial: "))
n2 = int(input("Ingresa la segunda nota parcial: "))
n3 = int(input("Ingresa la tercera nota parcial: "))
n4 = int(input("Ingresa la cuarta nota parcial: "))

final = (n1*0.2)+(n2*0.2)+(n3*0.2)+(n4*0.4)

print(f"La nota final del estudiante es: {final}" )