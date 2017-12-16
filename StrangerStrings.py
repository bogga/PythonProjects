import time
import os

def __print_alphabet(character):
    character = character.upper()
    charIndex = None
    row1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
    row2 = ["I", "J", "K", "L", "M", "N", "O", "P", "Q"]
    row3 = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    allRows = [row1, row2, row3]

    for row in allRows:
        for index, letter in enumerate(row):
            if character == letter:
                print("     " * index + "*", end='')
        print()
        for letter in row:
            print(letter + "    ", end='')
        print("\n")


def stranger_strings(string):
    for letter in string:
        os.system('cls')
        __print_alphabet(letter)
        time.sleep(2)

stranger_strings("HEY GEORGE")