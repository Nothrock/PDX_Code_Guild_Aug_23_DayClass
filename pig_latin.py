# get a word
# word = input('Let\'s translate a word to Pig Latin. Enter any word: ')
# split first letter from word so we have 2 parts

def pig_latin(word):
    vowels = 'aeiou'
    consonant = -1

    for letter in word:
        if letter.lower() in vowels:
            break
        else:
            consonant += 1

    first_letter = word[0:consonant + 1]
    left_over = word[consonant + 1:]
    #list vowels

    # compare first letter to list of vowels
    if first_letter.lower() in vowels:
        #if true add word + 'yay'
        return('{0}yay'.format(word))
    else:
        if first_letter[0].isupper():
            return('{0}{1}ay.'.format(left_over.capitalize(), first_letter.lower()))
        else:
            return('{0}{1}ay.'.format(left_over, first_letter))
