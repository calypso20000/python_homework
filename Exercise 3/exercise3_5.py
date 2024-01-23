# Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).

h=input("Write a string: ")
if len(h)>=2:
    newst=h[-2:]*4
    print(newst)
else:
    print("Length must be at least 2")