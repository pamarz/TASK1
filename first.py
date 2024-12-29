# Hangman game
import random
def hangman():
    word_list = ["python", "java", "javascript", "c++", "ruby"]
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    while tries > 0:
        print("Guess the word:")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("\n")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            tries -= 1
            print("Incorrect guess.")

        if "_" not in "".join([letter if letter in guessed_letters else "_" for letter in word]):
            print("Congratulations, you win!")
            break

    if tries == 0:
        print("You lose. The word was:", word)

hangman()
