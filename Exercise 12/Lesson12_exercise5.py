# Exercise 5: Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.

def onen(n):
    
    summ=0
    for i in range(1, n+1):
        summ+=i**2
    return summ

n=3
print(onen(n))