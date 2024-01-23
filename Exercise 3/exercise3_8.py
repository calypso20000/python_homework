# Create a string made of the first, middle and last character of given string with odd number of symbols

u=input("Type world: ")
if len(u)%2==1:
    middle=len(u)//2
    z=u[0]+u[middle]+u[-1]
    print(z)
else:
    print("Type odd number of symbols: ")