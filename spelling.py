#find e in a string (not the first letter though)
#check if next letter is i
# check if previous letter is c
#if i comes next and c does not come before e, print Remember, i before e except after c

def i_b4_e(word):
    word = word.lower()
    with open('i_e_exceptions.txt', 'r') as file:
        exceptions = file.read().replace('\n', ' ').split()
    if 'i' in word and word not in exceptions:
        for i in range(1, len(word)):
            if word[i] == 'i' and (word[i-1] == 'e' or word[i+1] == 'e'):
                if word[i+1] == 'e' and word[i-1] == 'c':
                    return False
                else:
                    return True
    else:
        return True


def c_grammar():
    g_check = input('Enter a word: ')
    if i_b4_e(g_check):
        print('Good job!')
    else:
        print('Remember, i before e except after c, or when sounding like A, as in neighbour or weigh!')

c_grammar()