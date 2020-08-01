"""
Problem Description
The program takes a list and removes the ith occurrence of the given word in the list where words can repeat.
Problem Solution
1. Take the number of elements in the list and store it in a variable.
2. Accept the values into the list using a for loop and insert them into the list.
3. Use a for loop to traverse through the elements in the list.
4. Then use an if statement to check if the word to be removed matches the element and the occurrence number and otherwise it appends the element to another list.
5. The number of repetitions along with the updated list and distinct elements is printed.
6. Exit.
"""
a=[]
n=int(input("Enter the size of list: "))
for i in range(n):
	elements=input(f"Enter elements of array at position {i}: ")
	a.append(elements)
print("elements of the list: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
c=[]
count=0
b=input("Enter word to remove: ")
n=int(input("Enter the occurrence to remove: "))
for i in a:
	if i==b:
		count=count+1
		if count!=n:
			c.append(i)
	else:
		c.append(i)
if count==0:
	print("Item not found")
else:
	print(f"The number of repetitions is: {count}")
	print(f"updated list is: {c}")
	print(f"The distinct elements are: {set(a)}")