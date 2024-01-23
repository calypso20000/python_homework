# Write a python program to add text to a file and display the text in python.txt.

def pythonn(dispfile):

    with open(dispfile, "r", encoding='utf-8') as news:
        c=news.read()
        print(c)

path ="C:/Users/missg/python.txt"
print(pythonn(path))