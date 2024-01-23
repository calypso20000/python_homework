# Turn every item of a list into its square

list=[5, 7, 3, 9, 11]
new_list=[]
for item in list:
    square=item**2
    new_list.append(square)

print(new_list)