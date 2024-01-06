# Write your code below this line 👇
import math


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.
# The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


# 🚨 Don't change the code below 👇
test_h = int(input('What is the height?\n'))  # Height of wall (m)
test_w = int(input('What is the with width?\n'))  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
