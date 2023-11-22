# While input example

# While loop example 1) Make user type in their name

name = input('What is your name?\n')

# This line will continue as long as it is true. Meaning as long as the user doesnt type in their name then the while loop will run forever
while name == '':
    print('You did not enter your name')
    # to break 'infinity loop'
    name = input('What is your name?\n')

# This line of code will run until the above condition is no longer true
print(f'Hello {name}')
