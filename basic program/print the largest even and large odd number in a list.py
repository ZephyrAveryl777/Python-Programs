#Python Program to print the largest even and largest odd number in a list.
n = int(input("Enter the number of elements to be in the list: "))
l=[]
for i in range(0,n):
	a=int(input(f"Enter the elements at position {i} in the list is:  "))
	l.append(a)
even=[]
odd=[]
for i in l:
	if i%2 == 0:
		even.append(i)
	else:
		odd.append(i)
even.sort()
odd.sort()
count_even =0
count_odd =0
for k in even:
	count_even += 1
for j in odd:
	count_odd += 1
print(f"largest even number in list {l} is {even[count_even-1]}")
print(f"largest odd number in list {l} is {odd[count_odd-1]}")