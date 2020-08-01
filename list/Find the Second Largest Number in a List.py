"""
Problem Description
The program takes a list and 
prints the second largest number in the list.
Problem Solution
1. Take in the number of elements and store it in a variable.
2. Take in the elements of the list one by one.
3. Sort the list in ascending order.
4. Print the second last element of the list.
5. Exit.
"""
a=[]
n=int(input("Enter the length of elements: "))
for i in range(0,n):
	b=int(input("Enter elements of the array: "))
	a.append(b)
#Display the elements
print("elements in the array: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
a.sort()
print(f"second largest element in array is: {a[n-2]}")
