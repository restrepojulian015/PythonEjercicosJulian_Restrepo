
answer = "no"

while answer.lower() == "no":
    edad = int(input("Ingresa tu edad: "))

    if(edad < 18):
        print(f"tu edad es de {edad} y no eres mayor de edad ")
    elif (edad >= 18 and edad <= 65):
        print(f"tu edad es de {edad} y eres mayor de edad")
    else:
        print(f"tu edad es de {edad} y eres jubilado")
    answer = input("¿Quierés salir?: ")