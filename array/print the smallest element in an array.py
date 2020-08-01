""" 
In this program, we need to find out the smallest element present in the array. 
This can be achieved by maintaining a variable min which initially will hold the value of the first element. 
Loop through the array by comparing the value of min with elements of the array. 
If any of the element's value is less than min, store the value of the element in the min.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at position {i}: "))
	arr.append(x)
print("elements of the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#Initialize min with the first element of the array
min=arr[0]
#loop through the array
for i in range(n):
	if arr[i]<min:
		min=arr[i]
print(f"Smallest element present in the given array: {min}")