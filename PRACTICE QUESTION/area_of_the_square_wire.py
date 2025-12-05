# A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42. The wire is converted into a square. Find the area of the square.


import math
arc = 60
arc = (arc/180)*math.pi
r = 42

length = r*arc

a = length/4

area = a*a

print("area of square : ",area)