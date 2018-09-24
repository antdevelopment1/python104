print("I am thinking of a number between 1 and 10. ")
user_input = int(input("What is the number? "))
guess = 8
correct = False

while correct == False:

    if user_input == guess:
        print("That was correct!!!")
        correct = True

    elif  user_input > guess:
        print("Too high of a number. Guess again!!!")
        user_input = int(input("What is the number? "))

    elif user_input < guess:
        print("Too low of a number. Guess again!!!")
        user_input = int(input("What is the number? "))