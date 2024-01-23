# Write a Python program to find if a given string starts with a given character using Lambda.


def find(given_string, given_character):
    a=lambda b, c: b[0]==c
    return a(given_string, given_character)

print(find("Kali", "k"))


# def find(given_string, given_character):
#         if given_string[0]==given_character:
#             return True
#         else:
#             return False
    
# print(find("kali", "k"))