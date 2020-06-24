# 321810304042-python_assignment_5

# Bhavyasree N - 321810304042


#     1.   Write a Python program to find area of a circle using math function.

import math
r=float(input("enter radius:"))
area=math.pi*r*r
print("area of circle:",area)



#     2.   Write a program to find Area of Regular Polygon using math function.

# METHOD_1 :

import math
n = float(input("number of sides: "))
s= float(input("length of a side: "))
p = n * (s** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is: ",p)

# METHOD_2 :

from math import tan,pi
n = int(input("number of sides: "))
s= float(input("length of a side: "))
area = n * (s** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ",area)



#      3.   Write a python program to find  Area of a Segment of a Circle Formula using math function.

r=int(input('Radius:'))
from math import pi
x=float(input('Angle:'))
area=(pi*r**2)*(x/360)
print('Area of segment of a circle :',area)



#      4.   Write a python program to shuffle list l1=[100,1,2,3,30,40,”hai”,”hello”].

import random
list11= [100,1,2,3,30,40,"hai","hello"]
random.shuffle(list11)
print(list11)



#      5.   Write a python program to generate random numbers between 1,10000 and difference between each random number is 50.

# METHOD_1 :

import random
rnum = random.randrange(1, 110000,50)
print("Random integer: ", rnum)

# METHOD_2 :

import random
print(" A random number from range is :")
print(random.randrange(1,10000,50))



#      6.   Write a python program by using math module to find : 
#  Sin600
#  cos(pi)
#  tan900
#  angle of sin(0.8660254037844386)
#  5^8
#  Square root of 400
#  The value of 5^e
#  The value of Log(1024), base 2
#  The value of Log(1024), base 10
#  The Floor and Ceiling value of 23.56 

import math
print(math.sin(math.pi/3)) 
print(math.cos(math.pi)) 
print(math.tan(math.pi/2)) 
print(math.sin(0.8660254037844386))
print(math.pow(5, 8))
print(math.sqrt(400))
print(math.exp(5))
print(math.log2(1024))
print(math.log10(1024))
print(math.floor(23.56),math.ceil(23.56))