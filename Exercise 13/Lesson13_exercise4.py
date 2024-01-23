# Write a Python program to find intersection of two given arrays using Lambda.

def two_given(a, b):
    c = list(filter(lambda r: r in a, b))
    return c

a = [1, 9, 4, 6, 7, 2, 8]
b = [3, 5, 7, 1, 9]

print(two_given(a, b))
