#chapter_4_reverse_sentence

#Write a function which takes a sentence as input and returns
#the reverse order of the words.

def reverse_sentence():
    sentence = input('Enter a sentence: ')
    split_list = sentence.split()
    print(' '.join(split_list[::-1]))

reverse_sentence()

