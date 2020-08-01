from array import * 
arr=array("i",[])
n=int(input("Enter the length of the input: "))
for i in range(n):
	x=int(input(f"Enter the element in the array at position {i}: "))
	arr.append(x)
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
#updating an element in the array
p=int(input("Enter the position of the element to be updated: "))
e=int(input("Enter the value of the element to be updated to: "))
arr[p] = e
print("Array after updation is : ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()