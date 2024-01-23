# Write a Python function to calculate the factorial of a number(a non-negative integer).The function accepts the number as an argument.

def factorial(n):
   if n<0:
      return "Please type a non-negative integer. Thank you. "
   else:
    result=1
    for i in range(1,n+1):
            result*=i
    return result
         
d=factorial(5)
print(d)
