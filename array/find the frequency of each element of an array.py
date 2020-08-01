"""
In this program, we need to count the occurrence of each unique element present in the array. 
One of the approach to resolve this problem is to maintain 
one array to store the counts of each element of the array. 
Loop through the array and count the occurrence of each element and store it in another array.
Program to find the frequency of each element of an array [1,2,8,3,2,2,2,5,1]
In the above array, 1 has appeared 1 time, so, the frequency of 1 is 1. 
Similarly, 2 has appeared 4 times. The frequency of 2 is 4 and so on.
""" 
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the element in the array at position {i}:  "))
	arr.append(x)
print("Elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()

#array fr will store frequencies of element 
fr=[None]*n
visited=-1
for i in range(n):
	count = 1
	for j in range(i+1,n):
		if arr[i]==arr[j]:
			count=count+1
			#to avoid counting same element again
			fr[j]=visited
	if fr[i] != visited:
		fr[i]=count

#Display the frequency of each element present in array
print("------------------")
print("Element | Frequency")
print("-------------------")
for i in range(n):
	if fr[i]!= visited:
		print(f"  {str(arr[i])} | {str(fr[i])}")
print("------------------")