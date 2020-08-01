print("-----------METHOD 1--------------")
#using clear() method
list=[]
n=int(input("Enter the size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements in the list before clearing: {list}")
list.clear()
print(f"elements in the list after clearing: {list}")

print("---------METHOD 2-------------")
"""
Reinitializing the list : 
The initialization of the list in that scope, 
initializes the list with no value. i.e list of size 0.
"""
list1=[]
n1=int(input("Enter size of first list: "))
for i in range(n1):
	data=int(input("Enter elements of list: "))
	list1.append(data)
print(f"elements of first list are: {list1}")
list2=[]
n2=int(input("Enter size of second list: "))
for i in range(n2):
	data=int(input("Enter elements of list: "))
	list2.append(data)
print(f"elements of second list are: {list2}")
#deleting list1 using clear()
list1.clear()
#printing list after clearing
print(f"elements of the first list after clearing using clear() are: {list1}")
#deleting list2 using Reinitializing
list2=[]
#printing list2 after Reinitializing
print(f"elements of the second list after Reinitializing: {list2}")

print(f"-------------------METHOD 3------------------------")
"""
Using *=0 
This is a lesser known method, but this method removes 
all elements of the list and makes it empty.
"""
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of list: "))
	list.append(data)
print(f"elements in the list are: {list}")
list *=	0
print(f"elements of the list after clearing using *=0 : {list}")

print("-------------METHOD 4---------------------")
#using del
"""
del can be used to clear the list elements 
in a range, if we don’t give a range,
all the elements are deleted.
"""
list1=[]
n1=int(input("Enter size of first list: "))
for i in range(n1):
	data=int(input("Enter elements of list: "))
	list1.append(data)
print(f"elements of first list are: {list1}")
list2=[]
n2=int(input("Enter size of second list: "))
for i in range(n2):
	data=int(input("Enter elements of list: "))
	list2.append(data)
print(f"elements of second list are: {list2}")
#deleting list1 using del
del list1[:]
print(f"elements of first list after cearing using del are: {list1}")
#deleting list2 using del
del list2[:]
print(f"elements of second list after cearing using del are : {list2}")