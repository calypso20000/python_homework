# Exercise 1: Counting Even Numbers
# Write a program that takes a list of numbers as input and counts the number of even numbers in the list. 
# Use a for loop, an if statement, and the modulus operator (%) to determine if a number is even or odd.

list = [2,3,4,6,7,8,9,11]
count = 0
for numb in list:
    if numb%2==0:
        count+=1

print("Number of even numbers", count)
