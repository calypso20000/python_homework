# Input three integers. 
# Output the word “Sorted” if the numbers are listed in a non-increasing or non-decreasing order and “Unsorted” otherwise.

a=input("Input integer 1: ")
b=input("Input integer 2: ")
c=input("Input integer 3: ")
if a<=b<=c>=a or a>=b>=c<=a:
    print("Sorted")
else:
    print("Unsorted")