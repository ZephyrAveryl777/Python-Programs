from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input(f'Enter the elements of the array at position {i}: '))
	arr.append(x)
print("Elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end=" ")
print()
start=int(input("Enter the staring position to slice the array: "))
end= int(input("Enter the ending position of the slicing array: "))
Slice_array = arr[start:end]
print(f"\nSlicing elements in a range : {Slice_array}")
Slice_array1 = arr[start: ]
print(f"\nSliced element from element at position {start} till the end: {Slice_array1}")
Slice_array2 = arr[:end]
print(f"\nSliced element till the position {end} : {Slice_array2}")
#printing elements from 
#beginig till end
Sliced_array = arr[:]
print(f"\nprinting all elements using slice operation: {Sliced_array}")