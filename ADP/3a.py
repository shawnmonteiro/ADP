'''Guess the Number: Write a program that tells the player that it has come up with a secret number and will give the player six chances to guess it. The code that lets the player enter a guess and checks that guess is in a for loop that will loop at most six'''

import sys
import random

r=random.randint(1,100)
guess=5

while(guess>=0):
    guessno=int(input("Enter your guessing number: "))
    if(guessno==r):
        print("Congratulations, you guessed the secret number "+str(r))
        sys.exit()
    elif(guessno<r):
        print("It's too low")
    else:
        print("It's too high")
    guess-=1

print("Sorry, better luck next time")
