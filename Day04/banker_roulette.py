names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

#import the random module
import random
#set the random number based on the number of indexes
name_index = len(names)
# Generate random numbers between 0 and the last index
random_index = random.randint(0, name_index - 1)
# print(random_index)
print(f"{names[random_index]} is going to buy the meal today!")

