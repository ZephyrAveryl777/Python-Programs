"""
In this program, we need to print the elements of the array which are present in odd positions. 
This can be accomplished by looping through the array and printing the elements of an array by
incrementing i by 2 till the end of the array is reached.
"""
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at position {i}: "))
	arr.append(x)
#Displaying the elements of the array
print("elements of the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#elements of the array at odd position
#looping through the array by incrementing the value of i by 2
print("elements at the odd positions are: ",end=" ")
for i in range(1,n,2):
	print(f"{arr[i]} => position({i}), ",end=" ")
print()
