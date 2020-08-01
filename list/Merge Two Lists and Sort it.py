"""
Problem Description
The program takes two lists, 
merges them and sorts the merged list.
Problem Solution
1. Take in the number of elements for the first list and store it in a variable.
2. Take in the elements of the list one by one.
3. Similarly, take in the elements for the second list also.
4. Merge both the lists using the ‘+’ operator and then sort the list.
5. Display the elements in the sorted list.
6. Exit.
"""
a=[]
c=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
	b=int(input("Enter elements of array: "))
	a.append(b)
n1=int(input("Enter the number of elements: "))
for i in range(n1):
	d=int(input("Enter elements of array: "))
	c.append(d)
new=a+c
new.sort()
print(f"Sorted list is: {new}")