# Count how many uppercase and lowercase characters are in this sentence.(“The Quick Brown Fox”)

sent =("The Quick Brown Fox")
split_str=sent.split()
l=0
u=0
for i in sent:
    if i.isupper():
        l+=1
    if i.islower():
        u+=1
print(l)
print(u)