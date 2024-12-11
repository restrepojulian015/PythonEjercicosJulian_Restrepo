#Ejercico para calcular cuantos puntos se obtuvo a partir de los ganados y empatados
ganados = int(input("Ingresa por favor cuantos partidos gano el equipo "))
empatados = int(input("Ingresa por favor cuantos partidos empato el equipo "))

total = (ganados*3)+ empatados

print(f"El puntaje global del equipo es: {total}")