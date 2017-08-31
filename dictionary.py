students = {
    'Watters': {'name': 'Kasey Watters', 'phone': 0000000000},
    'Magnuson': {'name': 'Tom Magnuson', 'phone': 1111111111},
    'Yeany': {'name': 'Johnny Yeaney', 'phone': 2222222222},
    'Tickle': {'name': 'Test Tickle', 'phone': 3333333333},
}

while True:
    query = input("Press 1 to search dictionary, 2 to add an entry, 3 to change an entry, 4 to delete an entry, 5 to display updates made this session, and 6 to exit: ")
    if query == '1':
        name = input('What\'s the last name of the student you are you looking for? ')
        print(students[name]['name'])
        print('({}) {}-{}'.format(str(students[name]['phone'])[0:3], str(students[name]['phone'])[3:6], str(students[name]['phone'])[6:]))
    elif query == '2':
        first_name = input('Type the new student\'s first name: ')
        last_name = input('Type the new student\'s last name: ')
        phone_number = input('Type the new student\'s phone number as shown: 8885551212: ')
        students.update({last_name: {'name': first_name + ' ' + last_name, 'phone': phone_number}})
        print(students)
    elif query == '3':
        change_name = input('Type the last name of the student whose information you wish to change: ')
        new_firstname = input('Type the student\'s new first name: ')
        new_lastname = input('Type the student\'s new last name: ')
        new_phone = input('Type the student\'s new phone number: ')
        del students[change_name]
        students.update({new_lastname: {'name': new_firstname + ' ' + new_lastname, 'phone': new_phone}})
        print(students)
    elif query == '4':
        name_gone = input('Type the last name of the student whose information you wish to delete: ')
        confirmation = input('Are you sure you wish to delete this information? press 1 to continue: ')
        if confirmation == '1':
            del students[name_gone]
        print(students)
    elif query == '5':
        print(students)
    elif query == '6':
        print('Goodbye')
        exit()
