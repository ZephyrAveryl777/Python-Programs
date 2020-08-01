"""
Problem Description
The program takes a list and swaps the first and last value of the list.

Problem Solution
1. Take the number of elements in the list and store it in a variable.
2. Accept the values into the list using a for loop and insert them into the list.
3. Using a temporary variable, switch the first and last element in the list.
4. Print the newly formed list.
5. Exit.
"""
print("---------------------------METHOD 1----------------------")
a=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
	data=int(input(f"Enter elements of the array at position {i}: "))
	a.append(data)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(f"New list: {a}")

print("---------------------METHOD 2-----------------------------")
"""The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1]"""
#Swap function
def swaplist(newList):
	newList[0], newList[-1]=newList[-1],newList[0]
	return newList
newList=[]
n=int(input("Enter the number of elements in the list: "))
for  i in range(n):
	data=int(input(f"Enter elements of the array at position {i}:  "))
	newList.append(data)
print(swaplist(newList))

print("---------------METHOD 3-------------------------")
"""Swap the first and last element is using tuple variable. 
Store the first and last element as a pair in a tuple variable, 
say get, and unpack those elements with first and last element in that list. 
Now, the First and last values in that list are swapped."""
#Swap function
def swaplist(list):
	#Storing the first and last element
	#as a pair in a tuple variable get
    get=list[-1],list[0]
    #unpacking those elements
    list[0],list[-1]=get
    return list
newList=[]
n=int(input("Enter the number of elements in the list: "))
for  i in range(n):
	data=int(input(f"Enter elements of the array at position {i}:  "))
	newList.append(data)
print(swaplist(newList))

print("-------------METHOD 4--------------------------")
"""Using * operand.
This operand proposes a change to iterable unpacking syntax, 
allowing to specify a “catch-all” name which will be assigned
a list of all items not assigned to a “regular” name."""
#usage of *operand
def swaplist(list):
	start, *mid, end = list
	list=[end, *mid, start]
	return list
newList=[]
n=int(input("Enter the number of elements in the list: "))
for  i in range(n):
	data=int(input(f"Enter elements of the array at position {i}:  "))
	newList.append(data)
print(swaplist(newList))

print("----------------METHOD 5-----------------------")
"""
Swap the first and last elements is to use inbuilt function list.pop(). 
Pop the first element and store it in a variable. 
Similarily pop the last element and store it in another variable.
Now insert the two popped element at each other’s original position.
"""
def swaplist(list):
	first=list.pop(0)
	last=list.pop(-1)
	list.insert(0,last)
	list.append(first)
	return list

newList=[]
n=int(input("Enter the number of elements in the list: "))
for  i in range(n):
	data=int(input(f"Enter elements of the array at position {i}:  "))
	newList.append(data)
print(swaplist(newList))
