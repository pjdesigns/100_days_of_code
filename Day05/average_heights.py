# Input a Python list of student heights
student_heights = input("What are the heights of the students? ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height

print(f"total height = {total_height}")

number_of_students = len(student_heights)
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")




