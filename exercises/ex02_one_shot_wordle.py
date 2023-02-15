"""EX02: One shot wordle."""
__author__ = "730313069"

secret_word: str = "python"
guess_word: str = input(f"What is your { len(secret_word) }-letter guess? ")
index: int = 0
emoji_string: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
character_exists: bool = False
alt_index: int = 0

while len(guess_word) != len(secret_word): #while loop until correct number of letters guessed
   guess_word: str = input(f"That was not { len(secret_word) } letters! Try again: ")
if guess_word == secret_word:
        print(int(len(secret_word)) * GREEN_BOX)
        print("Woo! You got it! ")
        exit()
else: # correct letter word that isnt the secret
        while index < len(secret_word):
                if secret_word[index] == guess_word[index]: #matching letters, same index
                        emoji_string += GREEN_BOX
                else: #letters dont match @ index
                        character_exists = False
                        alt_index = 0
                        while alt_index < len(secret_word) and character_exists is False: 
                                if secret_word[alt_index] == guess_word[index]:
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
exit()    