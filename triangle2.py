user_input = int(input("Please enter a number for the height of your triangle: "))
rows = user_input
for star in range(rows):
    print(' '*(rows-star+1) + '*'*(2*star+1))
print()
