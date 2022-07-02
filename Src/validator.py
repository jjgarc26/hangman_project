from random_word_generator import encrypted_version, hangman_word, chars_in_word

current_encrypted_version = chars_in_word

def check_for_letter(letter):
    for i in range(0, len(hangman_word) - 1):
        if letter == hangman_word[int(i)]:
            current_encrypted_version[int(i)] = hangman_word[int(i)]
        else:
            continue
    return current_encrypted_version






