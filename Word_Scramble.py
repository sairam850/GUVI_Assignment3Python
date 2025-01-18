#Word Scramble

#Import Random Module

import random

#Getting User Greetings
name = input("Enter your Name")
print("Good Start!", name)

#List of Words to be choosen from Random Words
words = ["python","javascript","java","automation","pytest","guvi","selenium"]
word = random.choice(words)

#Prompting the user to guess
print("Guess the characters")

#Initialising Guess and Turns
guesses = ''
turns = 15

#Using While Loop to Guess Attempts

while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end = "  ")
        else:
            print("_")
            failed = failed+1
    if failed == 0:
        print("You Won the Game")
        print("You found the word",word)
        break
    
    print()
    guess = input("Enter a character")

    guesses = guesses + guess

    if guess not in word:
        turns = turns-1
        print("Wrong Word Found")
        print("You have", +turns, "more guesses")

        if turns == 0:
            print("You have lost the game")

    
