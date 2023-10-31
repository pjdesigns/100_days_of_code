# Printing on different lines can be done in two ways

# Here is the first way, create three seperate print statements
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# Another way is to use  '\n'. This will create a new line and able to utilize one print statement
#Be sure to use "" for the outer quotes of the print statement
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")


# String concatenation - combining two strings: Example below

first_name = 'James'
last_name = 'Johnson'
full_name = (first_name + ' ' + last_name)
print(full_name)

# String concatenation can also be accomplished by using f strings. F strings are setup by f""" then place variable in {}

full_name_f_string = (f"{first_name} {last_name}")
print(full_name_f_string)

# Input function

name = input('What is your name? ')
num_of_characters = len(name)

print(f"Your name is {name} and it has {num_of_characters} characters")