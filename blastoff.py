import time
user_input = int(input("Please choose a number between 1 and 20: "))
count = user_input
if user_input <= 20:
    while count > 0:
        print(count)
        time.sleep(1)
        count -= 1
    if count == 0:
        print(count, "Blastoff! Going to the moon!!!")
elif user_input > 20:
    while count > 20:
        pick_another = int(input("Please pick a number between 1 and 20: "))
        if pick_another <= 20:
            while pick_another > 0:
                print(pick_another)
                time.sleep(1)
                pick_another -= 1
                if pick_another == 0:
                    print(pick_another, "Blastoff! Going to the moon!!!")
                    count = 0
