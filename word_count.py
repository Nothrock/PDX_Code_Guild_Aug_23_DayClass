divine_words = {}

with open('divine_comedy.txt','r') as dc:
  for line in dc:
    word_list = line.replace(',','').replace('(','').replace(')','').replace('\'','').replace('.','').replace(';','').replace('!','').replace('"','').replace('?','').replace(':','').lower().split()
    for word in word_list:
      if word not in divine_words:
        divine_words[word] = 1
      else:
        divine_words[word] = divine_words[word] + 1


# def remove_stop_words(wordlist, stopwords):
#   return [word for word in wordlist if not in stopwords]


print('{:15}{:3}'.format('Word','Count'))
print('-' * 18)

for  word,occurance  in divine_words.items():
  print('{:15}{:3}'.format(word,occurance))