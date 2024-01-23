# Your task is to implement a program that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all three.
# The set of elements that are unique to each list (present in only one list).

list1=[1,8,5,7,9]
list2=[2,4,6,7,9]
list3=[8,10,9,11,7,4]
set1=set(list1)
set2=set(list2)
set3=set(list3)

all_three=set1&set2&set3
at_least_two=set1&set2|set1&set3|set2&set3
unique=set1^set2^set3


print(all_three)
print(at_least_two)
print(unique)