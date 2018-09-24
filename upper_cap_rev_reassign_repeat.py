# # Converts input passed by user into uppercase.
# upper_input = input("Please choose a string to uppercase: ")
# upper_input = upper_input.upper()
# print(upper_input)

# # Capitalizes the first letter of each word in a string passed by the user.
# cap_input = input("Please a string to caplitalize: ")
# cap_input = cap_input.title()
# print(cap_input)

# Reverses a string that is given by the user.
# string = "" 
# user_input = input("Please enter a string to be reversed: ")
# for letter in user_input: 
#     string = letter + string
# print(string)

# Changes the value of certain characters within a string passed by a user and reassigns
# those characters to 'numbers' that are string data types.
# user_input = input("Please pass a string to be changed: ").upper() # Prompts user for a string.
# uni_character = list(user_input) # Converts user's input into a list of indiviual characters. "Split"
# for letter in uni_character: # Loops though each letter in side user's input.
#     if letter == "A": # Checks to see if specified letter is in the user's input.
#         uni_character[uni_character.index('A')] = '4' # When there's a match we reassign the value at current index in loop of user's input.
#     elif letter == "E":
#         uni_character[uni_character.index('E')] = '3'
#     elif letter == "G":
#         uni_character[uni_character.index('G')] = '6'
#     elif letter == "I":
#         uni_character[uni_character.index('I')] = '1'
#     elif letter == "O":
#         uni_character[uni_character.index('O')] = '0'
#     elif letter == "S":
#         uni_character[uni_character.index('S')] = '5'
#     elif letter == "T":
#         uni_character[uni_character.index('T')] = '7'
# print("".join(uni_character)) # We join the result back together.

# Loops through user's input to multiply words containing vowels in a series of two by 5.
user_input = input("Please choose a word with with two values next to one another. ").upper() # Prompts user for input.
list_of_vowels = ["A", "E", "I", "O", "U"] # List of vowels to check for.
new_input = " " # Container that will hold new string.
letter_to_match = " " # Value that holds previous letter in loop that allows us to check for repeating letters.
for letter in user_input: # Loops through each letter in the user's input.
    if letter == letter_to_match: # If letter matches the previous letter added to new_input this code block excecutes.
       new_input += (letter * 4) # Multiplies current letter by 4 instead of 5. Previous letter added will count as fifth repeated character.
    elif letter != new_input: # If character is not a vowel it will be added to new_input.
        new_input += letter
    letter_to_match = letter # Holds the value of the previous looped indiviual letter character.
print(new_input) # Prints new and modified string.
        