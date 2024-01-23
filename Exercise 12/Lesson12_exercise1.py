# Exercise 1: Check Pangram Function
# Write a function that checks if a sentence is a pangram.

def is_pangram(sentence):
    all_english_letters = ["a", "b", "c","d", "e", "f", "g", "h","i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in all_english_letters:
        if i  not in sentence:
            return False
    return True

print(is_pangram("abcdefghijklmnopqrstuvwxyz"))