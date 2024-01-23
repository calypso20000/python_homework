# Write a Python program to remove duplicates from a list.

list=[25, 1,1, 13]
noduplicate=[]
for i in list:
    if i not in noduplicate:
        noduplicate.append(i)
print(noduplicate)