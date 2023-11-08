rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# importing random module
import random

#Creating a list that contains variables: rock, paper, scissiors
rock_paper_scissors = [rock, paper, scissors]
#Setting for user
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors'))
print(f"You chose: {rock_paper_scissors[user_choice]}")
# print(rock_paper_scissors[user_choice])

# Setting for the computer
num_items = len(rock_paper_scissors)
#Subtract one index
computer_choice = random.randint(0, num_items - 1)
print(f"Computer chose: {rock_paper_scissors[computer_choice]}")
# print(rock_paper_scissors[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win")
elif user_choice == 0 and computer_choice == 1:
  print('You lost')
elif user_choice == 1 and computer_choice == 0:
  print('You Win')
elif user_choice == 1 and computer_choice == 2:
  print('You lost')
elif user_choice == 2 and computer_choice == 0:
  print('You lost')
elif user_choice == 2 and computer_choice == 1:
  print('You Win')
elif user_choice == computer_choice:
  print('Draw')

