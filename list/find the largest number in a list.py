"""
Problem Description
The program takes a list and prints the largest number in the list.

Problem Solution
1. Take in the number of elements and store it in a variable.
2. Take in the elements of the list one by one.
3. Sort the list in ascending order.
4. Print the last element of the list.
5. Exit.
"""
a=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
	b=int(input(f"Enter the elements at position {i}: "))
	a.append(b)
a.sort()
print("Largest element is: ",a[n-1])