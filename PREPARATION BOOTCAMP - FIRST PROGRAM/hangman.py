import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)
word = random.choice(list(words))
penalties = 0
guessed_letters = []

while penalties <= 12:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if display == word:
        print("You win!")
        break

    guess = input("Guess a letter or the whole word: ").lower()

    if len(guess) > 1:
        if guess == word:
            print("You win!")
            break
        else:
            penalties += 5
            print("Wrong word! Penalties:", penalties)
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        penalties += 1
        print("Wrong letter! Penalties:", penalties)

if penalties > 12:
    print("You lose! The word was:", word)
