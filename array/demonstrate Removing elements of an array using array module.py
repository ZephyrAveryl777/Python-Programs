from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f"Enter the elements of the array at position {i}: "))
	arr.append(x)

print("Elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()

#using pop() to remove elements at any position.
p=int(input("Enter the position of the element which is to be popped: "))
print(f"The poped elements is : {arr.pop(p)}",end=" ")
#printing array after popping an element
print("The array after removing an element: ",end =" ")
for i in range(n-1):
	print(arr[i],end=" ")
# using remove() to remove 1st occurrence of 1 
arr.remove(1) 
  
# # printing array after removing 
# print ("The array after removing is : ", end ="") 
# for i in range (0, n-2): 
    #print (arr[i], end =" ") 