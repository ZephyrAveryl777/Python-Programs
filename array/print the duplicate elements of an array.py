"""
In this program, we need to print the duplicate elements present in the array. 
This can be done through two loops. 
The first loop will select an element and the second loop will iteration through the array,
by comparing the selected element with other elements.
If a match is found, print the duplicate element.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at poistion {i}: "))
	arr.append(x)
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#Search for duplicate elements
print("Duplicate elements in given array: ",end=" ")
for i in range(n):
	for j in range(i+1,n):
		if arr[i]==arr[j]:
			print(arr[j],end=" ")
print()