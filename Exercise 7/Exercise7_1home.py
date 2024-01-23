#Arrange string characters such that lowercase letters should come first

characters="meGaTakinOarIgu"
upp=[]
low=[]
for i in characters:
    if i.islower():
        low.append(i)
    if i.isupper():
        upp.append(i)
result=low+upp
fin="".join(result)
print(fin)