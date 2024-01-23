# Given a list of words, create a dictionary where keys are words, and values are their lengths, but only for words with lengths greater than 3.

words=["fundamental", "government", "heaven", "historic", "hi"]

dictionary={x:len(x) for x in words if len(x)>3}
print(dictionary)