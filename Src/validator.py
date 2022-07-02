from random_word_generator import hangman_word, chars_in_word

current_encrypted_version = chars_in_word
# function to remove * with user guess letter
def check_for_letter(letter):
    for i in range(len(hangman_word)):
        if letter == hangman_word[i]:
            current_encrypted_version[i] = hangman_word[i]
        else:
            continue
    return current_encrypted_version
