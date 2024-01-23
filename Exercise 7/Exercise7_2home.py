# Count all letters, digits, and special symbols from a given string

string="P@#yn26at^&i5ve"
chars=0
digits=0
symbol=0
for i in string:
    if i.isalpha():
        chars+=1
    if i.isdigit():
        digits+=1
    if not i.isdigit() and not i.isalpha():
        symbol+=1
print(chars)
print(digits)
print(symbol)