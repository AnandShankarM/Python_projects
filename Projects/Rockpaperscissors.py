#Project-4

import random
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

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? 0 for rock, 1 for paper or 2 for scissors? \n"))
print("You choose:")
if user_input >= 0 and user_input <=2:
    print(game_images[user_input])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0 :
    print("Oops. You chose a wrong number")
elif user_input == computer_choice:
    print("Its a tie")
elif ((user_input == 0 and computer_choice ==2) or
      (user_input == 2 and computer_choice == 1) or
      (user_input == 1 and computer_choice == 0)):
    print("You won")
else:
    print("You loose")