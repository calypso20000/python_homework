# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
# The character’s position doesn’t matter.

s1=input("short: ")
s2=input("long: ")

if s1.lower() in s2.lower():
    print(True)
else:
    print(False)