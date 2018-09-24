# Fizz Buzz Solved in a For Loop.

for number in range(1, 100 + 1):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
        print(number)
    elif number % 3 == 0:
        number = "Fizz"
        print(number)
    elif number % 5 == 0:
        number = "Buzz"
    else:
        print(number)

# Fizz Buzz Solved in a While Loop

number = 0
while number < 101:
    if number % 5 == 00 and number % 3 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
    
    
    