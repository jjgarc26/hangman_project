import random

# this file is used to store words used in hangman game and pick a random word

word_choice = ['hello world', 'good morning', 'have a nice day', 'thank you', 'hot dogs']
random_index = random.randint(0, (len(word_choice) - 1))
hangman_word = word_choice[random_index]

chars_in_word = []

for letter in hangman_word:
    if letter == " ":
        chars_in_word.append("-")
    else:
        chars_in_word.append("*")
encrypted_version = ''.join(chars_in_word)


