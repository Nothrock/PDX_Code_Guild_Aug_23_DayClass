divine_words = {}


#import operator

#thing = (sorted(thing, reverse=True, key=operator.itemgetter(1))))
with open('divine_comedy.txt', 'r') as dc:
    for line in dc:
        word_list = line.replace(',', '').replace('(', '').replace(')', '').replace('\'', '').replace('.', '').replace(';', '').replace('!', '').replace('"', '').replace('?', '').replace(':', '').lower().split()
        for word in word_list:
            if word not in divine_words:
                divine_words[word] = 1
            else:
                divine_words[word] = divine_words[word] + 1


print('{:15}{:3}'.format('Word', 'Count'))
print('-' * 18)

for word, occurrence in divine_words.items():
    print('{:15}{:3}'.format(word, occurrence))

    #thy, me, their, the, and, if, unto, i, you, in, not, they, as, was, are, by, of, at, thou, she, he, what, that, his, so, then, is, her, its, who, has, upon, on, were, which, it, when, with, to, from, this, had, him, but, us, there, those, be,