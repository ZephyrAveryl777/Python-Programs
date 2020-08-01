"""
In this program, we need to sort the given array in ascending order
such that elements will be arranged from smallest to largest.
This can be achieved through two loops. The outer loop will select an element, 
and inner loop allows us to compare selected element with rest of the elements.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of array: "))
for i in range(n):
	x=int(input("Enter the elements of the array: "))
	arr.append(x)
#Displaying the array
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#soritng of the array
for i in range(n):
	for j in range(i+1,n):
		if arr[i]>arr[j]:
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
print()
#displaying sorted array elements
print("elements in the sorted array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()