# Write a Python program that asks the user to enter a password. 
# Keep asking for the password until the correct password "secret" is entered. Provide appropriate feedback to the user.

input_pass=input("enter a password: " ) 
right="secret"
while True:
    if input_pass==right:
        print("Password is correct")
        break
    else:
        print("Password is incorrect. Let's try again: ")
        break