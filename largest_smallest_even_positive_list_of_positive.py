# Largest Number
# Given an list of numbers, print the largest of the numbers.
list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(max(list_of_numbers))

# Smallest Number
# Given an list of numbers, print the smallest of the numbers.
list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(min(list_of_numbers))

# Even Numbers
# Given an list of numbers, print each number in the list that is even.
list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for number in list_of_numbers:
    if number % 2 == 0:
        print(number)

# Positive Numbers
# Given an list of numbers, print each number in the list that is greater than zero.
list_of_numbers_pos = [-10, -20, -30, -40, -50, 60, 70, 80, 90, 100]

for numbers in list_of_numbers_pos:
    if numbers > 0:
        print(numbers)

# Positive Numbers II
# Given an list of numbers, create a new list which contains every number in the given list which is positive
list_of_numbers_pos = [-10, -20, -30, -40, -50, 60, 70, 80, 90, 100]
new_list = []
for numbers in list_of_numbers_pos:
    if numbers > 0:
        new_list.append(numbers)
print(new_list)