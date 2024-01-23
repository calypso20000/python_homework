# You are given four real numbers - the coordinates of two points on a plane. 
# The first two numbers are the x and y coordinates of the first point, 
# and the last two numbers are the x and y coordinates of the second point. 
# Output the length of the line segment bounded by the two points.

import math

x1=float(input("first point x: "))
x2=float(input("second point x: "))
y1=float(input("first point y: "))
y2=float(input("second point y: "))
length_of_the_line=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(length_of_the_line)