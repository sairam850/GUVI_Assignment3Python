#Guess Number

#Import Random Module

import random
#Setting up the Range for Minimum and Maximum Attempts
num_guess = random.randint(1,20) 

#Using While Loop to Guess Attempts

while True:
    user_guess = int(input())

    if user_guess < num_guess:
        print("Too Low, Try Again")
    elif user_guess > num_guess:
        print("Too High, Try Again")
    else:
        print("Congrats, You found correct Number")
        break

