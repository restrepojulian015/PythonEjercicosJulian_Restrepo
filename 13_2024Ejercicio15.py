# función que me permite calcular el promedio de tres números

def funcion(n1,n2,n3):
    notaF = (n1+n2+n3)/3
    return notaF
# Utilizo un print para escribir un texto, los inputs para capturar esos
# valores.
listen ="si"

while listen =="si":
    print("Ingresa 3 números: ")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
# Imprime el resultado
    print(f"El promedio es: {funcion(n1,n2,n3)}")
    listen = input("Quierés seguir ?:")