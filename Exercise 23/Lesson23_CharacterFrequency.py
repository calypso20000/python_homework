# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

word= "economics"
frequencies = {x: word.count(x) for x in word}
print(frequencies)