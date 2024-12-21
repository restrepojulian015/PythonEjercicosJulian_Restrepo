while True:#bubble algorithm
    numbers = []
    num1 = int(input("Please, enter a number : "))
    num2 = int(input("Now, a second number : "))
    num3 = int(input("finally, third number : "))
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)
    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    print(numbers)
    exit = input("Do you want to do again? (yes/no) : ").lower()
    while exit !="yes" and exit !="no":
        exit = input("invalid opcion, please enter a correct opcion (yes/no) : ").lower()
    if exit =="no":
        break