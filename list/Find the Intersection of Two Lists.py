def intersection(a,b):
	return list(set(a) & set(b))

def main():
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
	print(f"intersection of two lists is: {intersection(a,b)}")
main()