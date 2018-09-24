import random
random_num = 5 #random.randint(1, 10)

print("I am thinking of a number between 1 and 10. ")
user_input = int(input("Please guess a number? "))
        
correct_guess = False
limit_guess = 3
while correct_guess == False:
    if user_input == random_num:
        print("Yay you won!!!")
        ask_to_play = input("Would you like to play again? Y/N").lower()
        if ask_to_play == "y":
            user_input = int(input("Please guess a number? "))
        elif ask_to_play == "n":
            print("Thanks for playing.")
            correct_guess = True
    elif user_input != random_num:
        limit_guess -= 1
        print("No you have %d turns left" % limit_guess)
        if limit_guess > 0:
            user_input = int(input("Please guess a number? "))
        elif limit_guess == 0:
            print("Sorry you lost the game!!!")
            ask_to_play = input("Would you like to play again? Y/N").lower()
            if ask_to_play == "y":
                limit_guess = 3
                user_input = int(input("Please guess a number? "))
            elif ask_to_play == "n":
                print("Thanks for playing.")
                correct_guess = True