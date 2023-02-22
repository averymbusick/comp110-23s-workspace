"""Exercise 03: Wordle. """

__author__ = "730313069"

def contains_char(search_str: str, guess_char: str) -> bool:
    """Searches for the single character that is target_char within the search_str, returns True if target_char is found at any index of search_str."""
    assert len(guess_char) == 1  # makes sure that target_char is a single character
    index: int = 0
    while index < len(search_str):
        if search_str[index] == guess_char:
            return True
        else:
            index += 1
    return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
def emojified(guess_word: str, secret_word: str) -> str:
    """Returns emoji string with boxes coordinated to whether the character occurs in secret word or not and if its in the right place."""
    emoji_str: str = ""
    idx: int = 0
    assert len(guess_word) == len(secret_word)  # makes sure that the guess and secret are same numb of letters
    while idx < len(secret_word):
        if guess_word[idx] == secret_word[idx]:  # matching indexes
          emoji_str += GREEN_BOX
        else:  # run contain_char to see if the guess_word[idx] is found elsewhere
            if contains_char(secret_word, guess_word[idx]) is False:
              emoji_str += WHITE_BOX
            else:
              emoji_str += YELLOW_BOX
        idx += 1
    return emoji_str

def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess until a guess of the right length is provided."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET_WORD: str = "codes"
    game_turn: int = 1
    while game_turn <= 6:
        print(f"=== Turn {game_turn}/6 ===")
        final_guess: str = input_guess(len(SECRET_WORD))
        if str(final_guess) != str(SECRET_WORD):
            print(emojified(final_guess, SECRET_WORD))
            game_turn += 1
        else:
            print(emojified(final_guess, SECRET_WORD))
            print(f"You won in {game_turn}/6 turns!")
            game_turn = 100
    if game_turn == 7:
        print("X/6 - Sorry, try again tomorrow!")
    
if __name__ == "__main__":
    main()