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

# use function to roll the dice and return the result

# Alternative dice roll with 2 dice
# Give both individual roll and then print sum of the rolls


def Play(choice, amount):
    """Roll one or two dice, or exit when the player chooses no."""
    choice = choice.strip().lower()

    if choice == 'n':
        print('Thanks for playing!')
        return False
    if choice != 'y':
        print('Invalid choice. Please enter Y or N.')
        return True

    if amount == '1':
        dice_roll = random.randint(1, 6)
        print(f'You rolled a {dice_roll}.')
    elif amount == '2':
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print(f'You rolled a {dice_roll1} and a {dice_roll2}. Total: {dice_roll1 + dice_roll2}.')
    else:
        print('Invalid amount. Please choose 1 or 2.')
    return True


while True:
    choice = input('Would you like to roll the dice? (Y/N): ')
    amount = input('How many dice will you play with? (1 or 2): ') if choice.strip().lower() == 'y' else ''
    if not Play(choice, amount):
        break
        

 

