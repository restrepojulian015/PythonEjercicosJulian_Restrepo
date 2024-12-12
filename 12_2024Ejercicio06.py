salir = "no"

while salir.lower() == "no":
    num = int(input("Digite un número: "))

    if (num <= 10):
        for i in range(num +1) :
            print(i)
    else:
        print(f"El número {num} está fuera del rango 1-10")
    salir = input("¿Quierés salir?: ")