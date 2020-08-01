"""
In this program, we need to print the elements of the array in reverse order that is; 
the last element should be displayed first, followed by second last element and so on.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at position {i}: "))
	arr.append(x)
#displaying the origianl array
print("elements in the array: ",end=" ")
for i in  range(n):
	print(arr[i],end=" ")
print()
#Array in reverse order
print("Array in the reverse order: ",end=" ")
#loop through the array in reverse order
for i in range(n-1,-1,-1):
	print(arr[i],end=" ")
print()