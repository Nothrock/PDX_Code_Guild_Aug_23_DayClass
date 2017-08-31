def case_convert(word):
    first_letter = word[0]
    if first_letter[0].isupper():
        return ('{} is CamelCase'.format(word))
    elif first_letter[0].lower:
        return ('{} is snake_case'.format(word))
new_word = input('Enter a word: ')
print(case_convert(new_word))