# width = int(input("Please Enter a Width of your choice  : "))
# height = int(input("Please Enter a Height of your choice  : "))

# for width_input in range(1, width + 1):
#     for height_input in range(1, height + 1):
#         if(width_input == 1 or width_input == width or height_input == 1 or height_input == height):          
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#     print()

# size = 5
# width = int(input("width? "))
# height = int(input("height? "))
# brick = " *"
# space = "  "
# height_input= 0

# while height_input < height:
#    width_input= 0

#    if height_input== 0 or height_input== (height - 1):
#        row = brick * width
#    else:
#        row = ""

#        while width_input< width:

#            if (width_input== 0) or (width_input== (width - 1)):


#                row = row + brick
#            else:


#                row = row + space

#            width_input= width_input+ 1

#    print(row)
#    height_input= height_input+ 1

# height = int(input("How tall should the box be?"))
# width = int(input("How wide should the box be?"))
# row = 0
# while row < height:
#    if row == 0 or row == height-1:
#        print("*"* width, end = "")
#    elif row < height:
#        print("*" + " " * (width-2) + "*", end = "")
#    row += 1
#    print()
# width = int(input("Width? "))
# height = int(input("Height? "))

# row = 0
# col = 0
# while row < width:

#  while col < height:
#    if col == 0 or col == (height - 1):
#      print("*", end = "")
#    elif row > 0 or row > (width - 1):
#      print("  ", end = "")
#    else:
#      print("*", end = "")
#      col = col + 1
#      row = row + 1
#  print()
height = int(input('How tall should the box be?'))
width = int(input('How wide should the box be?'))
row = 0
while row < height:
   if row == 0 or row == height-1:
       print('*'* width, end = '')
   elif row < height:
       print('*' + ' '* (width-2) + '*', end = '')
   row += 1
   print()
