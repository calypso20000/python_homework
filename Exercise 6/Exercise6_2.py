# Exercise 2: Vowel Counter
# Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string. 
# Use a for loop, an if statement, and the in operator to check if a character is a vowel.

r=input("Write string: ")
count=0
for i in r:
    if i in "aeiouAEIOU":
        count+=1

print(count)