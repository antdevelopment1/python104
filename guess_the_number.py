message = print("I'm thinking of a number between 1 and 10.")
user_input = int(input("What is the number? "))
guess = 7
correct = False
while not correct: 
    if guess != user_input:
        user_input = int(input("That wasn't the right number. Please try again. "))
    elif user_input == guess:
        print("You guess the number correctly!!! Great job!!!")
        correct = True
    
        
        
