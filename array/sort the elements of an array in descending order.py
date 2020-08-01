"""
In this program, we need to sort the given array in descending order such that 
elements will be arranged from largest to smallest. 
This can be achieved through two loops. 
The outer loop will select an element, 
and inner loop allows us to compare selected element with rest of the elements.
"""
#Initialize array     
from array import *
arr =array("i",[]) 
n=int(input("Enter the length of the array; ")) 
for i in range(0,n):
	x=int(input(f"Enter the elements of the array at position {i}: "))
	arr.append(x)
temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ",end =" ");    
for i in range(0, n):     
    print(arr[i],end=" ")
print()    

#Sort the array in descending order    
for i in range(0, n):    
    for j in range(i+1, n):    
        if(arr[i] < arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;         
print();    
     
#Displaying elements of array after sorting    
print("Elements of array sorted in descending order: ",end=" ");    
for i in range(0, n):     
    print(arr[i],end=" ")
print()