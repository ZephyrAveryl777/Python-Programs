from array import *
n=int(input("Enter the length of the array: "))
arr=array("i",[])
for i in range(n):
	x=int(input("Enter the elements: "))
	arr.append(x)
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
n=int(input("Enter the element which is to be searched for: "))
print(f"The index of 1st occurence of number {n} is at position{arr.index(n)}",end=" ")

