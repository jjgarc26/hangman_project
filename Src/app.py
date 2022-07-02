from random_word_generator import hangman_word
from validator import check_for_letter, current_encrypted_version
from stages import stages

# Main game
print('Welcome to Hangman Game')
amount_of_chances = 7
stage_count = 0

# Where user will input there choice
while amount_of_chances > 0:
    print(stages[stage_count])
    print(amount_of_chances)
    print(current_encrypted_version)
    user_guess = input('Guess a letter: ')
    # If user is correct, we will reveal word in encrypted version
    if user_guess in hangman_word:
        check_for_letter(user_guess)
        # If user guesses all words, while loop will break to get out of loop
        if "*" not in ''.join(current_encrypted_version):
            break
    # If incorrect, will reduce amount of chances
    else:
        amount_of_chances -= 1
        stage_count += 1

if amount_of_chances == 0:
    print(f"Sorry, the word was: {hangman_word}")
else:
    print(f"congratulations, you solves the word:  {hangman_word}")