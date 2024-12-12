exit = "none"

while exit.lower() == "none":
    num = int(input("Please, enter a positive number: "))
    pair = 0
    odd = 0

    
    for i in range (num +1):
        if(i % 2 ==0):
            pair += 1
        else:
            odd += 1
    print(f"There are {pair} peers numbers and there are {odd}  odd numbers")
    exit= input("Do you want exit?: ")