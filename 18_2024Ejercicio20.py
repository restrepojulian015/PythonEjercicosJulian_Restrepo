datos = (("BAQ","Barranquilla"),("BGA","Bucaramanga"),("BOG","Bogota"),("CLO","Cali"),("CTG","Cartagena"),("MEDE","Medellin"),("PEI","Pereira"),("PSO","Pasta"))

salir = False

while not salir:

    codigo = input("Ingresa por favor el Código: ").upper()

    for i in range(len(datos)):
        if codigo == datos[i][0]:
            print(f"Ciudad: {datos[i][1]}")
            
    else:
        print("No encontrado: ")

    respuesta = input("¿Quierés salir?: ").lower()
    if respuesta == "si":
        salir = True
