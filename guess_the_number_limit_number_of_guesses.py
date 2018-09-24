import random
random_num = random.randint(1, 10)

print("I am thinking of a number between 1 and 10. ")
user_input = int(input("Please guess a number? "))
	    
correct_guess = False
limit_guess = 3
#What do we want - If the user won
while correct_guess == False:
    if user_input == random_num:
        print("Yay you won!!!")
        correct_guess = True
    elif user_input != random_num:
        limit_guess -= 1
        print("No you have %d turns left" % limit_guess)
        if limit_guess > 0:
            user_input = int(input("Please guess a number? "))
        elif limit_guess == 0:
            print("Sorry you lost the game!!!")
            correct_guess = True