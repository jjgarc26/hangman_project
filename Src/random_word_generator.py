# this file is used to store words used in hangman game and pick a random word

import random
from word_list import word_list

# use random library to get random index to pick out a random word
random_index = random.randint(0, (len(word_list) - 1))
hangman_word = word_list[random_index]

# split words into individual chars
chars_in_word = []

for letter in hangman_word:
    chars_in_word.append("*")
encrypted_version = ''.join(chars_in_word)


