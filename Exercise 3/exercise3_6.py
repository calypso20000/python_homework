# Write a Python function to get a string made of its first three characters of a specified string. 
#If the length of the string is less than 3 then return the original string.

m= input("Type your string: ")
if len(m)>=3:
    newworld=m[0:3]
    print(newworld)
else:
    print(m)