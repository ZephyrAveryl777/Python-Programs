print("-------------METHOD 1------------------")
"""
Using the reversed() built-in function.
In this method, we neither reverse a list in-place
(modify the original list), nor we create any copy of the list.
Instead, we get a reverse iterator which we use to cycle through the list.
"""
def reverse(list):
	return [ele for ele in reversed(list)]

list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements of list: "))
	list.append(data)
print(f"elements of the list: {list}")
print(f"Reverse of the list is: {reverse(list)}")

print("-------------METHOD 2--------------------")
"""
Using the reverse() built-in function.
Using the reverse() method we can reverse the contents 
of the list object in-place i.e., 
we don’t need to create a new list instead we just copy
the existing elements to the original list in reverse order.
This method directly modifies the original list.
"""
def reverse(list):
	list.reverse()
	return list
list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements of list: "))
	list.append(data)
print(f"elements of the list: {list}")
print(f"Reverse of the list is: {reverse(list)}")

print("---------------METHOD 3-------------------")
"""
Using the slicing technique.
In this technique, a copy of the list is made 
and the list is not sorted in-place. 
Creating a copy requires more space to hold 
all of the existing elements. 
This exhausts more memory.
"""
def reverse(list):
	new_List=list[::-1]
	return new_List
list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements of list: "))
	list.append(data)
print(f"elements of the list: {list}")
print(f"Reverse of the list is: {reverse(list)}")
