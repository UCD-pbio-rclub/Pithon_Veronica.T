#chapter_4_palindrome

#Write a function which asks the user for a string and prints out
#whether the string is a palindrome or not

def palindrome_detector():
    string_forward = input('Enter a string: ')
    string_reverse = ''.join(string_forward[len(string_forward)::-1])
    if string_forward == string_reverse:
        print("This is a palindrome!")
    else:
        print("this is not a palindrome :(")

palindrome_detector()
