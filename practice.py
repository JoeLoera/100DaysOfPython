#Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much would you like to tip? 10, 12, or 15? "))
# people = int(input("How many people will split the bill? "))
# bill_with_tip = tip / 100 * bill + bill
# perPerson = round(bill_with_tip / people, 2)
# perPerson = "{:.2f}".format(perPerson)
# print(f"Each person owes ${perPerson}")


# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')


# #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# #Write your code below this line 👇

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'. \n").lower()

# if choice1 == "left":
#     choice2 = input("You've come to a lake. There is an island in the middle of the lake. Tyle 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("It's a room full of treasure. You Win!")
#         else:
#             print("You enter a room of beasts. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over")      
# else:
#     print("You fell into a hole. Game Over.")

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

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    
    
    
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
    