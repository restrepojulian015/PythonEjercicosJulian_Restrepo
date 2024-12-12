import random

exit = "no"

while exit.lower() =="no":
    # Create a random number
    ran = random.randint(1,100)

    # gie you a  clue

    if (ran <= 25):
        
        print("I`ll give you a clue, the number is very small")
    elif(ran > 25 and ran <= 50):
        print("I`ll give you a clue, the number is small")
    elif(ran > 50 and ran <= 75):
        print("I`ll give you a clue, the number is near to 100")
    else:
        print("I`ll give you a clue, the number is too near to 100")

    num = None

    while num != ran: 
            # logic
            try:
                num = int(input("Please, enter a positive number: "))
                if num < 1:
                    print("Please enter a positive number")
                    continue
                if num < ran:
                     print("You`re low, Try again")
                elif num> ran:
                     print("you`re high, Try again")
            
            except ValueError:
                 print("Invalid input, Please enter a valid number")
    print("Congratulations! youǜe guessed the number")
exit = input("Do you want to play again?: ")


    