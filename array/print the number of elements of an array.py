"""
In this program, we need to count and print the number of elements present in the array.
Some elements present in the array can be found by calculating the length of the array.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at position {i}: "))
	arr.append(x)
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#Number of elements present in the array can be found by using len()
print(f"Number of elements present in given array: {len(arr)}")