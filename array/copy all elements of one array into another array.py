"""
In this program, 
we need to copy all the elements of one array into another. 
This can be accomplished by looping through the first array and store the elements of the first array 
into the second array at the corresponding position.
"""
n = int(input("Enter the elements of the array: "))
arr = input()   # takes the whole line of n numbers
l = list(map(int,arr.split(' '))) 
"""split those numbers with space( becomes ['2','3','6','6','5']) 
and then map every element into int (becomes [2,3,6,6,5]) """ 
#Create another array say arr1 with size of arr
arr1 = [None]*len(arr)
#Copying all elements of one array into another
for i in range(0,len(arr)):
	arr1[i] = arr[i]
#Display elements of original array arr
print("Elements of original array: ")
for i in range(0,len(arr)):
	print(arr[i])
print()
#Displaying elements of new array arr1
print("Elements of new array: ")
for i in range(0,len(arr1)):
	print(arr1[i])