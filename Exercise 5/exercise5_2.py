# Write a Python program to get the largest number from a list.

list=[1, 2, 1, 1]
maxx=list[0]
for number in list:
    if number>maxx:
        maxx=number
print(maxx)