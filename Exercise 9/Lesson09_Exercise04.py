# Exercise 4: Print the multiplication table of 5 using a for loop and f”strings”. The table should be printed up to 10.

print("5-ի բազմապատկման աղյուսակը։ ")
for i in range(1,11):
    multiplication=i*5
    print(f"{i} * 5 = {multiplication}")