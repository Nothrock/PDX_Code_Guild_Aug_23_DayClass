
from random import shuffle
def split_words(string):
     word_list = string.split(', ')
     shuffle(word_list)
     return word_list

playing = True

while playing:
     query = input("Press 1 to enter words, 2 to read story, 3 to exit: ")
     if query == '1':
         nouns = input('enter two nouns separated by commas: ')
         adjectives = input('enter two adjectives separated by commas: ')
         verb = input('enter a verb: ')
         nouns_list = split_words(nouns)
         adjectives_list = split_words(adjectives)
         verb_list = split_words(verb)
     elif query == '2':
         print("While in Vegas, one should avoid {} {}, and be sure to {}. Your {} {} is likely going to depend on it.".format(adjectives_list[1], nouns_list[0], verb_list[0], adjectives_list[0], nouns_list[1]))
     elif query == '3':
         print("Thanks for playing.")
         playing = False
     else:
         print('I dont understand that')
