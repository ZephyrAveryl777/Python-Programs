#Python Program to compute a polynomial equation given that the coefficients of the polynomial are stored in the list.
import math
print(f"Enter the coefficients of the from ax^3 + bx^2 + cx +d ")
list = []
for i in  range(0,4):
	a=int(input("Enter the coefficients: "))
	list.append(a)
x=int(input("Enter the value of x: "))
sum = 0
j = 3 
for i in range(0,3):
	while j>0:
		sum=sum+(list[i]*math.pow(x,j))
		break
	j=j-1
sum=sum+list[3]
print(f"The value of the polynomial is: {sum}")