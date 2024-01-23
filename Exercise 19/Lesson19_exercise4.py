# Write a function that takes two lists and returns a new list containing only the common elements (without using set)

def common(list1, list2):
    common_elements=[]
    for i in list1:
        if i in list2:
            common_elements.append(i)
    return common_elements
        
list1=[1,3,5,7,9]
list2=[2,4,5,7,6,8]
print(common(list1, list2))