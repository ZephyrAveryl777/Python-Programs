from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements into array at position {i}: "))
	arr.append(x)
print("Origianl elements of the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#Rotate the given array by n times towards left
t=int(input("Enter the number of times an array should be rotated: "))
for i in range(0,t):
	#stores the last element of the array
	last = arr[n-1]
	for j in range(n-1,-1,-1):
		#Shift element of array by one
		arr[j]=arr[j-1]
	#last element of array will be added to the end
	arr[0]=last
print()
#Display resulting array after rotation
print("Array after left rotation:  ",end=" ")
for i in range(0,n):
	print(arr[i],end=" ")
print()

