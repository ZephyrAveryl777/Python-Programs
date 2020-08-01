n= int(input("Enter the number of elements to be in the list: "))
even=[]
odd=[]
negative=[]
b=[]
for i in range(0,n):
	a=int(input("Enter the element: "))
	b.append(a)
print("Element in the list are: {}".format(b))
sum_negative = 0
sum_positive_even = 0
sum_positive_odd = 0
for j in b:
	if j > 0:
		if j%2 == 0:
			even.append(j)
			sum_positive_even += j
		else:
			odd.append(j)
			sum_positive_odd += j
	else:
		negative.append(j)
		sum_negative += j
print("Sum of all positive even numbersin the list, i.e {1} are: {0}".format(sum_positive_even,even))
print("Sum of all positive odd numbers in the list, i.e {1} are: {0}".format(sum_positive_odd,odd))
print("Sum of all negative numbers in the list, i.e {1} are: {0}".format(sum_negative,negative))