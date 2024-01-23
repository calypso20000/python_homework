# Exercise 3: Average Function
# Write a function that calculates the average of a list of numbers.

def average(numbers):
    num_len = len(numbers)
    sum_num = 0
    for num in numbers:
        sum_num += num
    average = sum_num / num_len
    return average


numbers = [2, 4, 6, 8]
print(average(numbers))