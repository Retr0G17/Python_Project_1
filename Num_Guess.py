#Guessing Number game 
#User has to guess a number between 1 and 100. 
# The user wins if they guess the correct number.
#Game gives user another try when incorrect guess.
#Game will tell you if your guess is too high or too low.

import random
secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input('Enter a number between 1 and 100: '))
        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            print('Congratulations! You guessed the correct number.')
            break
    except ValueError:
        print('Please enter a valid number.')
    




   
