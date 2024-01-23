# Write a python function which create dict from 2 lists with the same length

def dictlist(list1, list2):
    new_dict={}
    for i in range(len(list1)):
       new_dict[list1[i]]=list2[i]
    return new_dict

list1=[1,5,7,9]
list2=["a","b","c","d","e"]
result=dictlist(list1, list2)
print(result)