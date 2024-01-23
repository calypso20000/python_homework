# Exercise 3: Word Finder
# Write a program that takes a list of words and a target word as input.
# The program should find and print all words in the list that contain the target word. 
# Use a for loop, the in operator, and an if statement to check if the target word is present in each word in the list.


input_word=input("input a keyword: ")
words=["key", "hey", "night", "love", "local"]
for i in words:
    if input_word.lower() in i.lower():
        print(i)
else:
    print("Try other key")