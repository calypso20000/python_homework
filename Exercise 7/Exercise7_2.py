# Write a Python script that takes a list of words and return the longest word and the length of the longest one.


w=["monkey", "dificuld", "beautiful", "day"]
l=0
for word in w:
        if len(word) > l:
            longest = word
            l = len(word)
print(f"longest word is: {longest}")
print(f"lenght of longest word is: {l}")