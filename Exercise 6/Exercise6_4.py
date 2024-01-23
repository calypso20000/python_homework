# Exercise 4: Palindrome Checker
# Write a program that prompts the user to enter a word and checks if it is a palindrome. 
#A palindrome is a word that reads the same backward as forward. 
#Use string slicing and an if-else statement to compare the original word with its reverse.

h=input()
lower_word=h.lower()
if lower_word==lower_word[::-1]:
    print('word is polindrome')
else: 
    print("word is not polindrome")