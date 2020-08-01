"""
Problem Description
The program takes a list and finds the second largest number in the list using bubble sort.
Problem Solution
1. Take in the number of elements for the list and store it in a variable.
2. Take in the elements of the list one by one.
3. Then sort the list using bubble sort.
4. Print the second last element of the sorted list which is the second largest number.
5. Exit.
"""
a=[]
n=int(input("Enter the length of the elements: "))
for i in range(0,n):
	b=int(input(f"Enter elements of the array at position {i}: "))
	a.append(b)
print("elements of the array: ",end=" ")
for i in range(0,n):
	print(a[i],end=" ")
print()
#bubble sort the second largest number in the list
for i in range(0,n):
	for j in range(0,n-i-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
print(f"second largest number is: {a[n-2]}")
