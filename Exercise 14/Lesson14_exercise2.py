# Write a function in Python to count and display the total number of words in a text file.

def text_file(place):

    with open(place, 'r') as count:
        a = count.read()
        b = a.split()
        print(len(b))

path = 'D:\Python\BDG\homework\Lesson14\example.txt'
text_file(path)