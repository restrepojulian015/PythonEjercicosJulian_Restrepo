def fibonacci(n):
    
    if(n <=0):
        return 0
    elif(n ==1):
        return 1
    else:
        a = 0
        b = 1
        for i in range (n):
            a,b = b, a + b
        return print(f"El númnero es: {b}")



try:
     num = int(input("Igresa la posición del número Fibonacci: "))
     fibonacci(num)
except ValueError :
        print("ERROR: TIPO DE DATO")
