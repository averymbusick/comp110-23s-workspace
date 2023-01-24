"""EX01 Chardle - A cute step toward Wordle."""
__author__ = "730313069"

word: str = input("Enter a 5 character word: ")
if len(word) == 5:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character")
        exit()
    print("Searching for " + letter + " in " + word)
    repeats: int = 0
    if letter in word:
        if word[0] == letter:
            print(letter + " found at index 0")
            repeats += 1
        if word[1] == letter:
            print(letter + " found at index 1")
            repeats += 1
        if word[2] == letter:
            print(letter + " found at index 2")
            repeats += 1
        if word[3] == letter:
            print(letter + " found at index 3")
            repeats += 1
        if word[4] == letter:
            print(letter + " found at index 4")
            repeats += 1
        if repeats == 1:
            print(str(repeats) + " instance of " + letter + " found in " + word)
        else:
            print(str(repeats) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)
else:
    print("Error: Word must contain 5 characters")
    exit()