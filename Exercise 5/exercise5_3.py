# Write a Python program to get the smallest number from a list

list=[5, 7, 3, 9, 11]
smallest=list[0]
for numb in list:
    if numb<smallest:
        smallest=numb

print(smallest)