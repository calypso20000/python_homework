# Write a Python program that input a sentence and return the longest word and the length of the longest one.

r=input()
k=r.split()
length=0
for word in k:
    if len(word) > length:
        longest=word
        length=len(word)
print(k)
print(f"longest word is: {longest}")
print(f"lenght of longest word is: {length}")