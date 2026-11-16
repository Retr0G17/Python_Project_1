# Dice Roll Game
import random

# Ask User to roll the dice 
# If user enters Y/y
# Generate a random number between 1 and 6
# Print result of dice roll 

# if user selects N/n
#print Thanks for playing
# else 
# print invalid choice

# Alternative dice roll with 2 dice
# Give both individual roll and then print sum of

while True:
    choice = input('Would you like to roll the dice? (Y/N): ')
    amount = input('How many dice will you play with? (1 or 2): ')

    if choice == 'y' or choice == 'Y':
        if amount == '1':
            dice_roll = random.randint(1, 6)
            print(f'You rolled a {dice_roll}.')
        elif amount == '2':
            dice_roll1 = random.randint(1, 6)
            dice_roll2 = random.randint(1, 6)
            print(f'You rolled a {dice_roll1} and a {dice_roll2}. Total: {dice_roll1 + dice_roll2}.' )
        else:
            print('Invalid amount.')
    elif choice == 'n' or choice == 'N':
        print('Thanks for playing!')
        break

    else:
        print('Invalid choice.')

 

