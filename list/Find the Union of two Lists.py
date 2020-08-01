"""
Problem Description
The program takes two lists and finds the unions of the two lists.
Problem Solution
1. Define a function which accepts two lists and returns the union of them.
2. Declare two empty lists and initialise to an empty list.
3. Consider a for loop to accept values for two lists.
4. Take the number of elements in the list and store it in a variable.
5. Accept the values into the list using another for loop and insert into the list.
6. Repeat 4 and 5 for the second list also.
7. Find the union of the two lists.
8. Print the union.
9. Exit.
"""
a=[]
n=int(input("Enter the size of first list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	a.append(data)
print("elements of the first list: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
b=[]
n1=int(input("Enter the size of second list: "))
for i in range(n1):
	data1=int(input("Enter elements of the list: "))
	b.append(data1)
print("elements of the second list: ",end=" ")
for i in range(n1):
	print(b[i],end=" ")
print()
union=list(set().union(a,b))
print(f"Union of two lists is: {union}")