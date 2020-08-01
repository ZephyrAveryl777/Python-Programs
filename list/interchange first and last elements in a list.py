"""
Given a list in Python and provided the positions of the elements, 
write a program to swap the two elements in the list.
"""
print("-----------------------------METHOD 1-------------------------------")
#simple swap
def swapPosition(list,pos1,pos2):
	list[pos1],list[pos2]=list[pos2],list[pos1]
	return list

list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input(f"Enter the element in the list at position {i+1}: "))
	list.append(data)
print("Before swapping elements in the lsit: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
pos1=int(input("Enter the first position: "))
pos2=int(input("Enter the second position: "))
print(f"After swapping elements from position {3} to position {1} in the list:  ",end=" ")
print(swapPosition(list,pos1-1,pos2-1))

print("----------------------------------METHOD 2-------------------------------------")
"""
Using Inbuilt list.pop() function
Pop the element at pos1 and store it in a variable. 
Similarly, pop the element at pos2 and store it in another variable. 
Now insert the two popped element at each other’s original position.
"""
def swapPosition(list,pos1,pos2):
	#popping both the elements from list
	first_element = list.pop(pos1)
	second_element = list.pop(pos2-1)

	#inserting in each others positions
	list.insert(pos1,second_element)
	list.insert(pos2,first_element)
	return list

list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input(f"Enter the element in the list at position {i+1}: "))
	list.append(data)
print("Before swapping elements in the lsit: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
pos1=int(input("Enter the first position: "))
pos2=int(input("Enter the second position: "))
print(f"After swapping elements from position {3} to position {1} in the list:  ",end=" ")
print(swapPosition(list,pos1-1,pos2-1))

print("---------------------METHOD 3-----------------------------")
"""
Using tuple variable
Store the element at pos1 and pos2 as a pair in a tuple variable, 
say get. Unpack those elements with pos2 and pos1 positions in that list.
Now, both the positions in that list are swapped.
"""
def swapPosition(list,pos1,pos2):
	#storing the two elements
	#as a pair in a tuple variable get
	get = list[pos1],list[pos2]
	#unpacking those elements
	list[pos2],list[pos1] = get
	return list
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input(f"Enter the element in the list at position {i+1}: "))
	list.append(data)
print("Before swapping elements in the lsit: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
pos1=int(input("Enter the first position: "))
pos2=int(input("Enter the second position: "))
print(f"After swapping elements from position {3} to position {1} in the list:  ",end=" ")
print(swapPosition(list,pos1-1,pos2-1))

print("-----------------------------METHOD 4-----------------------------")
#Using comma assignment
def swapPosition(list,pos1,pos2):
	list[pos1],list[pos2] = list[pos2],list[pos1]
	return list
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input(f"Enter the element in the list at position {i+1}: "))
	list.append(data)
print("Before swapping elements in the lsit: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
pos1=int(input("Enter the first position: "))
pos2=int(input("Enter the second position: "))
print(f"After swapping elements from position {3} to position {1} in the list:  ",end=" ")
print(swapPosition(list,pos1-1,pos2-1))

