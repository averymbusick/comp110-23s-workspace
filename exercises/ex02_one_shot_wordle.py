"""EX02: One shot wordle."""

__author__ = "730313069"

SECRET_WORD: str = "python"
guess_word: str = input(f"What is your { len(SECRET_WORD) }-letter guess? ")
index: int = 0
emoji_string: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
character_exists: bool = False
alt_index: int = 0

while len(guess_word) != len(SECRET_WORD): #while loop until correct number of letters guessed
    guess_word = input(f"That was not { len(SECRET_WORD) } letters! Try again: ")
if guess_word == SECRET_WORD:
    print(int(len(SECRET_WORD)) * GREEN_BOX)
    print("Woo! You got it! ")
    exit()
else: # correct letter word that isnt the secret
    while index < len(SECRET_WORD):
            if SECRET_WORD[index] == guess_word[index]: #matching letters, same index
                        emoji_string += GREEN_BOX
            else: #letters dont match @ index
                        character_exists = False
                        alt_index = 0
                        while alt_index < len(SECRET_WORD) and character_exists is False: 
                            if SECRET_WORD[alt_index] == guess_word[index]:
                                character_exists = True
                            else:
                                alt_index += 1
                        if character_exists != True:
                            emoji_string += WHITE_BOX
                        else:
                            emoji_string += YELLOW_BOX
            index += 1 #check 0 indice, then 1, 2, etc. until = len(secret_word)
    print(emoji_string)
print("Not quite. Play again soon! ")   