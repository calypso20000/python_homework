# Write a python function, which create a dictionary for given number N, where keys are numbers from 1 to N, 
# and values are cubs of that numbers

def dictn(n):
    cube={}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube

print(dictn(5))