print("---------METHOD 1------------")
#sort the list in ascending order and print the first element of the list.
list=[]
n=int(input("enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f'elements of the list are: {list}')
#sorting the elements of the list
list.sort()
print(f"the smallest elements of the list is: {list[0]}")

print("------------METHOD 2--------------")
#Using min() method
list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f'elements of the list are: {list}')
print(f'smallest element of the list is:{min(list)}')

print("--------------METHOD 3-----------------")
#using assigned min 
l=[l for l in (input('list: ').split(",")]
print(f"elements in the list are: {l}")
#assigning first elements of the list as minimum
min=l[0]
for i in range(len(l)):
	#if the other element is min than first element
	if l[i]<min:
		min=l[i]
print(f"smallest element of the list is {min}")