age = input('What is your age?\n')
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeks = 52
age_to_int = int(age)

weeks_to_90 = (90 - age_to_int) * 52
print(f"You have {weeks_to_90} weeks left.")