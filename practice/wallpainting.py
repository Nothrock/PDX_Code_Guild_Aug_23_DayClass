from math import ceil

wall_width = int(input('How many feet wide is the wall? '))
wall_height = int(input('How many feet high is the wall? '))
paint_cost_per_gallon = float(input('What is the price of paint per gallon? '))
number_of_coats = int(input('How many coats would you like to apply? '))
sq_feet = (wall_width * wall_height) * number_of_coats
gallons_paint_needed = ceil(sq_feet / 400)
total_cost = paint_cost_per_gallon * gallons_paint_needed
print('That is {} square feet.'.format(sq_feet))
print('You will need {} gallons of paint to apply {} coat(s) of paint to this wall.'.format(
    gallons_paint_needed,
    number_of_coats
))
print('It will cost you ${} to paint this wall.'.format(total_cost))
