#Guessing Number game 
#User has to guess a number between 1 and 100. 
# The user wins if they guess the correct number.
#Game gives user another try when incorrect guess.
#Game will tell you if your guess is too high or too low.

import random


guess = int(input('Enter a number between 1 and 100: '))
secret_number = random.randint(1, 100)

while guess != secret_number:
    if guess < secret_number:
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')
    guess = int(input('Enter a number between 1 and 100: '))

print('Congratulations! You guessed the correct number.')