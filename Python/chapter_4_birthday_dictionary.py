#chapter_4_birthday_dictionary

dictionary = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815'}

def birthday_dictionary():
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for key in dictionary:
        print(key)
    person = input("Who's birthday would you like to look up?")
    print(dictionary[person])

birthday_dictionary()
