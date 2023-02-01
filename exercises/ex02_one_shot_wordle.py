"""EX02: One shot wordle"""
__author__ = "730313069"

secret_word: str = "python"
guess_word: str = input(f"What is your { len(secret_word) }-letter guess? ")
letter_check: str = guess_word[0]
green_box: str = "\U0001F7E9"
while len(guess_word) != int(len(secret_word)):
   guess_word: str = input(f"That was not { len(secret_word) } letters! Try again: ")
if guess_word == secret_word:
        print(int(len(secret_word)) * green_box)
        print("Woo! You got it! ")
        exit()
else:
        print("Not quite. Play again soon. ")
        exit()    