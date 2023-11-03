# 1st input: enter height in meters e.g: 1.65
height = input('What is your height?\n')
# 2nd input: enter weight in kilograms e.g: 72
weight = input('What is your weight?\n')
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_to_int = float(height)
weight_to_int = float(weight)

bmi = round(weight_to_int / height_to_int ** 2)
print(f"Your bmi is {bmi}")
