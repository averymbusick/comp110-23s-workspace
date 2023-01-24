"""EX01 Chardle - A cute step toward Wordle."""
__author__ = "730313069"

word: str = input("Enter a 5 character word: ")
if len(word) == 5:
    letter: str = input("Enter a single character: ")
    print("Searching for " + letter + " in " + word)
    if letter in word:
        if word[0] == letter:
            print(letter + " found at index 0")
        if word[1] == letter:
            print(letter + " found at index 1")
        if word[2] == letter:
            print(letter + " found at index 2")
        if word[3] == letter:
            print(letter + " found at index 3")
        if word[4] == letter:
            print(letter + " found at index 4")
        print(str(word.count(letter)) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)
else:
    print("Error: Word must contain 5 characters")
    exit()