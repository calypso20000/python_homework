# Exercise 4: Find Index Function
# Write a function that finds the index of a given element in a list. If the element is not present, return -1.

def find_index(element, my_list):
   
    index = -1
    for i in range(len(my_list)):
        if my_list[i] == element:
            index = i
            break
    return index