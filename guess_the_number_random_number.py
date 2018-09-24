import random
random_num = random.randint(1, 10)

print("I am thinking of a number between 1 and 10. ")
user_input = int(input("Please guess a number. "))

correct_guess = False

while correct_guess == False:
    if random_num == user_input:
        print("Yay you guessed correctly!!!")
        correct_guess = True
    elif random_num != user_input:
        print("That was not correct.")
        user_input = int(input("Please guess again. "))

