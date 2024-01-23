#  Given a string, create a dictionary where keys are characters, and values are their ASCII values.

words="foundation"

dictionary={x:ord(x) for x in words}
print(dictionary)

