"""
Problem Description
The program takes a list and puts the even and odd elements in it into two separate lists.
Problem Solution
1. Take in the number of elements and store it in a variable.
2. Take in the elements of the list one by one.
3. Use a for loop to traverse through the elements of the list and an if statement to 
check if the element is even or odd.
4. If the element is even, append it to a separate list and if it is odd, 
append it to a different one.
5. Display the elements in both the lists.
6. Exit.
"""
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
	b=int(input("Enter the elements of the array: "))
	a.append(b)
even=[]
odd=[]
for j in a:
	if j%2 == 0:
		even.append(j)
	else:
		odd.append(j)
print(f"The even list: {even}")
print(f"The odd list: {odd}")