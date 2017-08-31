# Write a function to convert between `mi`, `km`, `ft`, and `m`.
#
# --------------------
#
# ##### Instructions
#
# Ask the user for a distance, then the units of that distance, then the target units.
# Then print out the conversion as below.
#
# ```
# > Enter a distance:
# > 100
# > Enter units:
# > mi
# > Enter target units:
# > km
# > 100 mi is 160.93440000000115 km
# ```
#
# Support converting between `mi`, `km`, `ft`, and `m`.
#
# ## Advanced
#
# *   Also support converting between `in` and `cm`.
#
# *   Also support converting between `gal` and `L`.
#     Error if someone tries to convert between volume and distance. Use `raise`.
#
# -------------------
#
# ## Super Advanced
#
# * Also support converting between all [metric prefixes](https://en.wikipedia.org/wiki/Metric_prefix) of meters.
#
# ------------------------
# #### Key Concepts
#
# - Variables
# - Function definition
# - User input
# - Built-In functions
# - Logic Problems
#

def convert_distance(dis, c_from, c_to):
    if c_from.lower() == 'mi':
        if c_to == 'km':
            return dis * 1.6
        elif c_to == 'ft':
            return dis * 5280
        elif c_to == 'm':
            return dis * 1609.344
        elif c_to == 'in':
            return dis * 63360
        elif c_to == 'cm':
            return dis * 160934
    elif c_from.lower() == 'km':
        if c_to == 'mi':
            return dis * .621371
        elif c_to == 'ft':
            return dis * 3280.84
        elif c_to == 'm':
            return dis * 1000
        elif c_to == 'in':
            return dis * 39370.1
        elif c_to == 'cm':
            return dis * 100000
    elif c_from.lower() == 'ft':
        if c_to == 'mi':
            return dis * .000189394
        elif c_to == 'km':
            return dis * .0003048
        elif c_to == 'm':
            return dis * .3048
        elif c_to == 'in':
            return dis * 12
        elif c_to == 'cm':
            return dis * 30.48
    elif c_from.lower() == 'm':
        if c_to == 'mi':
            return dis * .000621371
        elif c_to == 'km':
            return dis * .001
        elif c_to == 'ft':
            return dis * 3.28084
        elif c_to == 'in':
            return dis * 39.3701
        elif c_to == 'cm':
            return dis * 100
    elif c_from.lower() == 'in':
        if c_to == 'mi':
            return dis * 1.5783 * 10 ** -5
        elif c_to == 'km':
            return dis * .0000254
        elif c_to =='ft':
            return dis * .0833333
        elif c_to == 'm':
            return dis * .0254
        elif c_to == 'cm':
            return dis * 2.54
    elif c_from.lower() == 'cm':
        if c_to == 'mi':
            return dis * 6.21371 * 10 ** -6
        elif c_to == 'km':
            return dis * 1 * 10 ** -5
        elif c_to == 'ft':
            return dis * .0328084
        elif c_to == 'm':
            return dis * .01
        elif c_to == 'in':
            return dis * .393701


distance = int(input('Enter a distance: '))
convert_from = input('What unit of measurement is the distance currently'
                     '(you may enter mi, km, ft, m, in, cm)? ')
convert_to = input('What unit of measurement are we converting the distance to? ')
print('{} {} converts to {} {}.'.format(distance, convert_from, convert_distance(distance, convert_from, convert_to), convert_to))