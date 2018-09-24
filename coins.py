message = print("You currently have 0 coins.")
user_input = input("Would you like another? ").lower()
coin_count = 0
if user_input != "yes":
    print("Bye")
while user_input == "yes":
    coin_count += 1
    print("You have %d coins!!!" % coin_count)
    user_input = input("Would you like another? ").lower()
    
    