while True:#tell me if all are even or not
    try:
        num1 = int(input("Please, enter a number : "))
        num2 = int(input("Please, enter another number : "))
        if num1%2 == 0 and num2%2 ==0:
            print("both numbers are even")
        elif num1%2 !=0 and num2%2 != 0: 
            print("both number are odd")
        else:
                print("either of them are even")
    except ValueError:
        print("please, enter correct number ")
    exit = input("Do you want to do again ?: ").lower()
    while exit !="yes" and exit !="no":
        exit = input("Please, enter a correct opcion (yes/no) :")
    if exit.lower() =="no":
        break