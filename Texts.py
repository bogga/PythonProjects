def reverse_string(string):
    return string[::-1]

def __getFirstConsonantIndex(string):
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    for index, letter in enumerate(string):
        if letter not in vowels:
            return index

def piggie_dat_string(string):
    consIndex = __getFirstConsonantIndex(string)
    return string[consIndex + 1:] + string[0:consIndex + 1] + "ay"

def count_vowels(string):
    # it's worth noting this could be done with objects, it's just easier
    # (and saves lines) like this
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    counts = [0, 0, 0, 0, 0]
    for letter in string:
        for index, vowel in enumerate(vowels):
            if letter == vowel:
                counts[index] = counts[index] + 1

    return counts

def is_palindrome(string):
    pairs = len(string)
    place = 0
    for i in range(0, pairs):
        if string[place] != string[-place - 1]:
            return False
        place += 1
    return True

def count_words(string):
    string = string.split()
    count = 0
    for word in string:
        count += 1

    return count