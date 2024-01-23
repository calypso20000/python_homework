# Write a python program to read the whole text of a file and catch the error if files does not exists.

def proj(run):
    try:
        with open(run, "r") as file:
            s=file.read()
            print(s)

    except FileNotFoundError:
        print("Check file name, please")

path='D:/Python/BDG/homework/Lesson16/newtext.txt'
d=(proj(path))

