#This is a number guessing game.
#You input a number to guess if it matches a randomly selected number between 1 and 20.
#You will have 6 chances to numG the number.
import random
import os

print('Hello. What is your name?')
name = input()
numToGuess = random.randint(1,30)
totalChances = 10
print(name+', guess a number between 1 and 30: ')

for numOfGuesses in range(1,totalChances):
    numG = int(input())
    while(numG > 30 and numG > 0):
        print("Sorry, the value you entered is not between 1 and 20. Enter a valid number.")
        numG = int(input())
    if numG < numToGuess:
        print('Your guess is too low. Try again. You have '+str(totalChances-numOfGuesses)+' guesses left.')
    elif numG > numToGuess:
        print('Your guess is too high. Try again. You have '+str(totalChances-numOfGuesses)+' guesses left.')
    else:
        break

if numG == numToGuess:
    print('Congratulations '+name+'! You guessed the right number which is '+str(numToGuess)+'.')
    print('You took '+str(numOfGuesses)+' guesses to find the number.')
else:
    print('Sorry! You took too many guesses. The number to guess was '+str(numToGuess)+'.')

os.system("pause")