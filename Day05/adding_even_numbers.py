target = int(input('Enter a number between 0 and 1000\n')) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
#Adding +1 to target so the last index is included
for number in range(2, target + 1, 2):
  total += number
  # print(number)
  
print(total)
  