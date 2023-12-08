# Name : Nicholas vickery
# Date : 9/1/2023
# Project : Guessing Game
# Description : This game is made to let two players play. The first player sets the number and the second player has to guess that number.
#               The number choice is 1 through 100. Everytime the second player misses the number they have to keep re-trying til the number is guessed

import os 
import random 
# Hide the number function
def Hide(): 
    os.system("cls")


# Computer chooses random number
print(random.randrange(1,100))

# Hide the number
Hide()


# Player 2 turn
guessed = False
tries = 0
while not guessed:
    tries += 1
    # Player 2 guess the number
    guessNum = input("Player 2, please enter your guess: ")
    # If guess is too high, print too high
    if guessNum > mainNum: 
        print("Sorry, too high try again.")
    # if guess is too low, print too low
    if guessNum < mainNum: 
        print("Sorry, too low try again.")
    # If guess is correct, end game
    if guessNum == mainNum: 
        print("Thats correct, Great guess")
        guessed = True

# Number of guess it took player 2 to get to the correct number
print(f"Number of guesses : {tries}")