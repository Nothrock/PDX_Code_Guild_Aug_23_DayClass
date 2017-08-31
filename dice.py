from random import randint


def dice_game():

    dice_number = int(input('How many dice would you like to roll?: '))
    dice_sides = int(input('Choose how many sides the dice will have. You may choose from 4, 6, 8, 10, 12, and 20 sided dice: '))
    while dice_number > 0:
        print('You\'ve rolled a', randint(1,dice_sides))
        #dice_number = dice_number -1
        dice_number -= 1

dice_game()