"""
In this program, we need to print the element which is present on even position. 
Even positioned element can be found by traversing the array and incrementing the value of i by 2.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at position {i} :  "))
	arr.append(x)
#Displaying elements of the array:
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#elements of the array at even position
print("elements of given array present on even position are: ",end=" ")
#Loop through the array by incrementing the value of i by 2
for i in range(0,n,2):
	print(f"{arr[i]}",end= " ")
print()