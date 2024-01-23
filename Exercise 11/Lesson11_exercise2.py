# Write a Python function to calculate count of each letter in string

def count_letter(inputt):
    result={}
    for letter in inputt:
        if letter.isalpha():
            if letter in result:
                result[letter]+=1
            else:
                result[letter]=1
    return result

inputt="Calypso"
result=count_letter(inputt)
print(result)