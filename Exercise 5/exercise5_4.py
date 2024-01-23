# Write a Python program to find the second smallest number in a list.

list=[1, 10, 5, 7]
smallest=10000
second_smallest=10000
for number in list:
    if number<smallest:
        second_smallest=smallest
        smallest=number
    elif number<second_smallest:
        second_smallest=number
print(second_smallest)