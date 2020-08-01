"""
In this program, we need to calculate the sum of all the elements of an array. 
This can be solved by looping through the array and add the value of the element 
in each iteration to variable sum.
""" 
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at  position {i}: "))
	arr.append(x)
print("elements of the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#to find sum
sum = 0
for i in range(n):
	sum=sum+arr[i]
print(f"Sum of all the elements of an array: {sum}")