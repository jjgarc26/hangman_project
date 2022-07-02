from random_word_generator import hangman_word, encrypted_version
from validator import check_for_letter, current_encrypted_version

# This will display the person's life span
print('Welcome to Hangman Game')
amount_of_chances = 6

while amount_of_chances > 0:
    print(amount_of_chances)
    print(current_encrypted_version)
    user_guess = input('Guess a letter: ')
    if hangman_word.find(user_guess):
        check_for_letter(user_guess)
    else:
        amount_of_chances -= 1

print(hangman_word)
print(encrypted_version)
nw = encrypted_version.replace('o', encrypted_version[2])
print(nw)
