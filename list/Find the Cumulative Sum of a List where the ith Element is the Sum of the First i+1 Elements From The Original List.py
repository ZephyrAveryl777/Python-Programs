"""
Problem Description
The program takes a list from the user and finds the cumulative 
sum of a list where the ith element is the sum of the first i+1 elements from the original list.
Problem Solution
1. Declare an empty list and initialise to an empty list.
2. Consider a for loop to accept values for the list.
3. Take the number of elements in the list and store it in a variable.
4. Accept the values into the list using another for loop and insert into the list.
5. Using list comprehension and list slicing, find the cumulative sum of elements in the list.
6. Print the original list and the new list.
7. Exit.
"""
a=[]
n=int(input("Enter the number of elements in list: "))
for i in range(n):
	data=int(input(f"Enter elements at position {i}: "))
	a.append(data)
print("elements in the list: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
b=[sum(a[0:i+1]) for i in range(0,n)]
print(f"The new list is: {b}")