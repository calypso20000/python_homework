# Input two positive integers, and output a line describing their relation. Follow the sample format.

a=input("positive integer 1: ")
b=input("positive integer 2: ")
if a>b:
    print(f"{a} > {b}")
if a<b:
    print(f"{a} < {b}")
if a==b:
    print(f"{a} = {b}")