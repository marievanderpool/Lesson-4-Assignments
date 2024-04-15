# Objective: The aim of this assignment is to explore the random package in Python 
# and understand how it can be used with loops to introduce randomness into your programs.

# Task 1: Random Choice Game Create a game where a player has a list of items. 
# They have to guess which item in the list was selected. Use random.choice() to select 
# the item and take the user's guess via input. Provide feedback on whether they guessed 
# correctly or not keep them playing until they guess correctly.

import random

items = ['bubble blower', 'basketball', 'tiara']

selected_item = random.choice(items)

while True:
    guess = input("Guess which item was highlighted: ")     
    if guess == selected_item:
        print("Congratulations! You guessed right.")
        break
    else:
        print("Sorry, that's wrong. Try Again!")