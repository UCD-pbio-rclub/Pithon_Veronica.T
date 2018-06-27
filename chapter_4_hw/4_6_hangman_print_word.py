#4_5_hangman_play

import random
words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 14
guessed_letters = ''

def pick_a_word():
    return random.choice(words)

print(pick_a_word())

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The word was: ' + word)
            break

def get_guess(word):
    return 'a'

def process_guess(guess, word):
    global lives_remaining
    global guessed_letters
    lives_remaining = lives_remaining -1
    guessed_letters = guessed_letters + guess
    return False

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or whole word?')
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    print(display_word)

play()
