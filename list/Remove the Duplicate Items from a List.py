"""
Problem Description
The program takes a lists and removes the duplicate items from the list.

Problem Solution
1. Take the number of elements in the list and store it in a variable.
2. Accept the values into the list using a for loop and insert them into the list.
3. Use a for loop to traverse through the elements of the list.
4. Use an if statement to check if the element is already there in the list and if it is not there, append it to another list.
5. Print the non-duplicate items of the list.
6. Exit.
"""
a=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input(f"Enter elements of array at position {i}: "))
	a.append(data)
print("elements in the list: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
b=set()
unique=[]
for i in a:
	if i not in b:
		unique.append(i)
		b.add(i)
print(f"List without duplicate elements are: {unique}")