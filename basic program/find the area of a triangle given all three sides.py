# Python Program to find the area of a triangle given all three sides.
import math
a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area of the triangle is: {round(area,2)}")