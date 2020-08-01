# Python program to demonstrate 
# Adding Elements to a Array 

# importing "array" for array creations 
from array import * 

# array with int type 
arr = array('i', [])
n=int(input("Enter the length of the array:  "))
for i in range(n):
	x=int(input("Enter the elements of the array: "))
	arr.append(x)

print("Elements in the array : ", end =" ") 
for i in range (0, n): 
	print (arr[i], end =" ") 
print() 

# inserting array using 
# insert() function
p=int(input("Enter the position where the value has to be inserted starting from 0: "))
v=int(input("Enter the value to be inserted: "))

arr.insert(p,v) 
print("Array before insertion : ", end =" ") 
for i in range (0, n): 
	print (arr[i], end =" ") 
print()

print ("Array after insertion : ", end =" ") 
for i in (arr): 
	print (i, end =" ") 
print() 

# array with float type 
b = array('d', [2.5, 3.2, 3.3]) 

print ("Array before insertion : ", end =" ") 
for i in range (0, 3): 
	print (b[i], end =" ") 
print() 

# adding an element using append() 
b.append(4.4) 

print ("Array after insertion : ", end =" ") 
for i in (b): 
	print (i, end =" ") 
print() 
