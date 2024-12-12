# calcula las Àreas 
import math

print("Bienvenido al menu")
print("1) Para Calcular el área de un cuadrad0")
print("2) Para Calcular el área de un trinagulo")
print("3) Para Calcular el área de un Circulo")
option = int(input("Dime tu respuesta: "))
try:
    if option == 1:
        a = float(input("Ingresa Por favor un lado"))
        suma = a*a
        print(F"EL ÀREA ES IGUAL A {suma} cm  ")
    elif option ==2:
        base = float(input("Ingresa por favor la base: "))
        altura = float(input("Ingresa por favor la altura: "))
        area = (base * altura)/2
        print(f"El area del triangulo es igual a {area} cm cuadrados")
    elif option == 3:
        rad = float(input("Ingresa por favor el radio: "))
        area = math.pi * (rad ** 2)
        print(f"EL Àrea es {area} radianes")
except ValueError:
    print("Dato de tipo String, por favor ingresa un dato entero o de tipo float")