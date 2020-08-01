print("---------METHOD 1------------")
"""
Using slicing technique
This is the easiest and the fastest way to clone a list. 
This method is considered when we want to modify a list 
and also keep a copy of the original. 
In this we make a copy of the list itself,
along with the reference. This process is also called cloning.
This technique takes about 0.039 seconds and is the fastest technique
"""
def Cloning(list):
	list_copy=list[:]
	return list_copy

list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
list1=Cloning(list)
print(f"After cloning elements in the list are: {list1}")

print("-------------METHOD 2---------------")
"""
Using the extend() method
The lists can be copied into a new list by using the extend() function. 
This appends each element of the iterable object (e.g., anothre list) 
to the end of the new list. 
This takes around 0.053 second to complete.
"""
def Cloning(list):
	list_copy=[]
	list_copy.extend(list)
	return list_copy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
list1=Cloning(list)
print(f"After cloning elements in the list are: {list1}")

# print("-------------METHOD 3---------------------")
# def Cloning(li1):
# 	list_copy=list(li1)
# 	return list_copy
# li1=list_copy=[]
# n=int(input("Enter size of list: "))
# for i in range(n):
# 	data=int(input("Enter elements of the list: "))
# 	li1.append(data)
# print(f"elements in the list are: {li1}")
# li2=Cloning(li1)
# print(f"After cloning elements in the list are: {li2}")

print("-------------------METHOD 4------------------")
def Cloning(list):
	list_copy=[i for i in list]
	return list_copy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
list1=Cloning(list)
print(f"After cloning elements in the list are: {list1}")

print("-------------------METHOD 5 -----------------------")
"""
Using the append() method
This can be used for appending and adding elements
to list or copying them to a new list. 
It is used to add elements to the last position of list. 
This takes around 0.325 seconds to complete and 
is the slowest method of cloning.
"""
def Cloning(list):
	list_copy=[]
	for item in list: list_copy.append(item)
	return list_copy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
list1=Cloning(list)
print(f"After cloning elements in the list are: {list1}")

print("-------------------METHOD 6 --------------------")
"""
Using the copy() method
The inbuilt method copy is used to copy 
all the elements from one list to another. 
This takes around 1.488 seconds to complete.
"""
def Cloning(list):
	list_copy=[]
	list_copy=list.copy()
	return list_copy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
list1=Cloning(list)
print(f"After cloning elements in the list are: {list1}")

print("---------------------METHOD 7-----------------------")
"""
Using shallow copy 
A shallow copy creates a new object which 
stores the reference of the original elements.
So, a shallow copy doesn't create a copy of nested 
objects, instead it just copies the reference of
nested objects. This means, a copy process does not 
recurse or create copies of nested objects itself.
"""
import copy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
new_list=copy.copy(list)
print(f"elements in the list after cloning are: {new_list}")

print("---------------METHOD 8----------------------")
"""
A deep copy creates a new object and recursively
adds the copies of nested objects present in 
the original elements.
"""
import copy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
new_list=copy.deepcopy(list)
print(f"elements in the list after cloning are: {new_list}")