"""
Problem Description
The program removes all tuples in a list of tuples with the USN outside the given range.
Problem Solution
1. Take in the lower and upper roll number from the user.
2. Then append the prefixes of the USN’s to the roll numbers.
3. Using list comprehension, find out which USN’s lie in the given range.
4. Print the list containing the tuples.
5. Exit.
"""
a=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
	data=[input("Enter a character: "),input("Enter roll number with sequence 16CS: ")]
	a.append(data)
print("Elements of the list: ",end=" ")
for i in range(n):
	print(a[i],end=" ")
print()
low=int(input("Enter lower roll number (starting with 16CS): "))
up=int(input("Enter upper roll number (starting with 16CS):  "))
l='16CS0'+str(low)
u='16CS'+str(up)
p=[x for x in a if x[1]>l and x[1]<u]
print(p)