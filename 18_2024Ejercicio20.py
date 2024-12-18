datos = (("BAQ","Barranquilla"),("BGA","Bucaramanga"),("BOG","Bogota"),("CLO","Cali"),("CTG","Cartagena"),("MEDE","Medellin"),("PEI","Pereira"),("PSO","Pasta"))

salir = False

while not salir:
    city = ''

    codigo = input("Ingresa por favor el Código: ").upper()
    for cod,nom in datos:
        if cod == codigo:
            city = f"Ciudad: {nom}"
    if len(city) ==0:
        print("Código no encontrado")
    else:
        print(city)

    respuesta = input("¿Quierés salir?: ").lower()
    if respuesta == "si":
        salir = True
