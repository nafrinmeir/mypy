#Step 1 

#word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-1
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = (random.choice(word_list))
print(chosen_word)

#TODO-2
guess = input('Guess a letter:').lower()
print(guess)

for c in range(0, len(chosen_word)):
    if chosen_word[c] == guess:
        print(chosen_word[c], end="")
    elif chosen_word[c] == " ":
        print(" ", end="")
    else:
        print("-", end="")