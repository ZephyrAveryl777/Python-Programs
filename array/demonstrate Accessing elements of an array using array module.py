from array import *
arr = array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
	x=int(input("Enter the elements of the array: "))
	arr.append(x)
print("elements in the array: ",end=" ")
for i in range(n):
	print(arr[i],end =" ")
print()

""" For accessing the elements in an array"""
while 1:
	p= int(input("Enter the position of the array you want to access: "))
	print(f"Accessing element at position {p} : {arr[p]}")
	print("type n to exit the accessing! type y to continue the accessing!")
	option= input("Enter your choice: ")
	if option == "n":
		break
	elif option =="y":
		continue
	else:
		print("Invalid choice, accessing auto aborted!")
		break