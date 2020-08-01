""" 
 In this program, we need to find out the largest element present in the array and display it.
 This can be accomplished by looping through the array from start to end by 
 comparing max with all the elements of an array. 
 If any of element is greater than max, then store a value of the element in max. 
 Initially, max will hold the value of the first element. 
 At the end of the loop, max represents the largest element in the array.
 """
from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
 	x=int(input(f"Enter the elements of the array at position {i}: "))
 	arr.append(x)
 #Displaying the array elements
print("Elements of the array: ",end=" ")
for i in range(n):
 	print(arr[i],end=" ")
print()
 #Initalize the max with the first element of array
max=arr[0]
#Loop through the array
for i in range(n):
	#compare elements of array with max
	if arr[i]>max:
		max=arr[i]
print(f"Largest element present in given aray: {max}")