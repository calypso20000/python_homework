# Write a python program to catch error a num dividing by zero.

def num_dividing(a,b):
    
    try: return a/b
    except ZeroDivisionError:
        print("You can't dividing by zero number")

print(num_dividing(12,6))