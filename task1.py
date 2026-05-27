import os

# User enters the secret word
secret_word = input("Enter the secret word: ").lower()

# Clear screen
os.system('cls')

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while incorrect_guesses < max_incorrect_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet only.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess!")
        print("Remaining Chances:", max_incorrect_guesses - incorrect_guesses)

if incorrect_guesses == max_incorrect_guesses:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman Game!")