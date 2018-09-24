grid_size = int(input("Enter a number to display a grid. "))

row = 0
while row < grid_size:
    col = 0
    while col < grid_size:
        print("*", end="")
        col += 1
    row += 1
    print()

