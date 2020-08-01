"""
Problem Description
The program takes a list of lists and sorts the list according to the second element in the sublist.
Problem Solution
1. Take in a list containing sublists.
2. Using two for loops, use bubble sort to sort the sublists based on the second value of the sublist.
3. If the second element of the first sublist is greater than the second element of the second sublist, exchange the entire sublist.
4. Print the sorted list.
5. Exit.
"""
a=[]
n=int(input("Enter the number of elements in the array: "))
for i in range(n):
	ele=[input("Enter elements: "),int(input("followed by integer: "))]
	a.append(ele)
#Origianl elements in the list
print("elements in the list: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
#sorting list according to the second element in the sublist
print("After sorting the elements accoring to the second element of the sublist:  ",end="  ")
for i in range(n):
	for j in range(0,n-i-1):
		if a[j][1]>a[j+1][1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
print(a,end=" ")
print( )
