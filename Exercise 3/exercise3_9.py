# Append new string in the middle of a given (even number of characters) string

j=input()
if len(j)%2==0:
    string=input("Append new string: ")
    middle=len(j)//2
    new_string=j[:middle]+string+j[middle:]
    print(new_string)
else:
    print("even number of characters")