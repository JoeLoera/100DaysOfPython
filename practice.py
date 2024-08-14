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

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice > 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_images[user_choice])
    
#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])
    
    
    
#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose!")
#     elif computer_choice > user_choice:
#         print("You lose!")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw!")
    

# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# # password = ""
# # #nr_letters = 4
# # for char in range (1, nr_letters + 1):
# #     password += random.choice(letters)

# # for char in range (1, nr_symbols + 1):
# #     password += random.choice(symbols)

# # for char in range (1, nr_numbers + 1):
# #     password += random.choice(numbers)

# # print(password)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_list = []

# for char in range (1, nr_letters + 1):
#     password_list += random.choice(letters)

# for char in range (1, nr_symbols + 1):
#     password_list += random.choice(symbols)

# for char in range (1, nr_numbers + 1):
#     password_list += random.choice(numbers)

# print(password_list)

# random.shuffle(password_list)
# print(password_list)

# password= ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")

#Code for moving robot around the maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
# import random

# from hangman_words import word_list
# from hangman_art import stages, logo

# lives = 6

# print(logo)

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)

# game_over = False
# correct_letters = []

# while not game_over:

#     print(f"****************************{lives}/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()

#     if guess in correct_letters:
#         print(f"You've already guessed {guess}")

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print("Word to guess: " + display)

#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")

#         if lives == 0:
#             game_over = True

#             print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

#     if "_" not in display:
#         game_over = True
#         print("****************************YOU WIN****************************")

#     print(stages[lives])


# # 1: Import and print the logo from art.py when the program starts.
# import art
# print(art.logo)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # 2: What happens if the user enters a number/symbol/space?


# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:

#         if letter not in alphabet:
#             output_text += letter
#         else:
#             if encode_or_decode == "decode":
#                 shift_amount *= -1

#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")


# # 3: Can you figure out a way to restart the cipher program?

# should_continue = True

# while should_continue:

#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye")


# import art

# def add(n1, n2):
#     return n1 + n2

# #TODO Write out the 3 other functions - subtract multiple and divide

# def subtract(n1,n2):
#     return n1 - n2

# def multiply(n1,n2):
#     return n1 * n2

# def divide(n1,n2):
#     return n1 / n2

# #ToDo Add these 4 functions to a dictionary
# operators_dict = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# #ToDo Use the dictionary operations to perform the calculations. Multiply 4*8 using dictionary

# # print(operators_dict["*"](4,8))


# def calculator():
#     print(art.logo)
#     should_accumulate = True
#     num1 = float(input("What is the first number?: "))

#     while should_accumulate:
#         for symbol in operators_dict:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operators_dict[operation_symbol](num1,num2)
#         print(f"{num1}{operation_symbol}{num2} = {answer}")

#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation ")

#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
# calculator()


import random
import art
def deal_card():
    #returns a random card from the deck
    cards = [10,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    #Take a list of cards and return a caclulated score
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponenet has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def playgame():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    print("\n" * 20)
    playgame()