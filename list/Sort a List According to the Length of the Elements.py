"""
Problem Description
The program takes a list and sorts the list according to the length of the elements.
Problem Solution
1. Take in the number of elements for the first list and store it in a variable.
2. Take in the elements of the list one by one.
3. Then sort the list giving the length of the elements as the key.
4. Display the sorted list.
5. Exit.
"""
a=[]
n=int(input("Enter the length of the list: "))
for i in range(n):
	x=(input(f"Enter elements of array at position {i}: "))
	a.append(x)
print("elements of the array: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
#sorting the list
a.sort(key=len)
print("list after sorting is: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
