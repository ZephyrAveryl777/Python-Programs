"""
In this program, we need to rotate the elements of an array towards the left by the specified number of times. 
In the left rotation, each element of the array will be shifted to its left by one position and 
the first element of the array will be added to end of the list. 
This process will be followed for a specified number of times.
"""
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
	#stores the first element of the array
	first = arr[0]
	for j in range(0,n-1):
		#Shift element of array by one
		arr[j]=arr[j+1]
	#First element of array will be added to the end
	arr[n-1]=first
print()
#Display resulting array after rotation
print("Array after left rotation:  ",end=" ")
for i in range(0,n):
	print(arr[i],end=" ")
print()

print("----------------Method 2-------------")
"""
Juggling Algorithm.
This is an extension of method 1. Instead of moving one by one, divide the array in different sets
where number of sets is equal to GCD of n and d and move the elements within sets.
"""
def leftRotate(arr, d, n): 
    d = d % n 
    g_c_d = gcd(d, n) 
    for i in range(g_c_d): 
          
        # move i-th values of blocks  
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
  
# UTILITY FUNCTIONS 
# function to print an array  
def printArray(arr, size): 
    print("\nArray after left rotation : ",end=" ")

    for i in range(size): 
        print ("% d" % arr[i], end =" ") 
print()
  
# Fuction to get gcd of a and b 
def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a % b) 
  
# Driver program to test above functions  
arr = array("i",[]) 
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input("Enter the elements in the array: "))
	arr.append(x)
print("Elements in the array:",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
d = int(input("Enter the number by which the array to be rotated: "))
leftRotate(arr, d, n) 
printArray(arr, n) 
