print("--------------METHOD 1 using Loop--------------------")
#NAIVE METHOD
"""
In Naive method, one easily uses a loop 
that iterates through all the elements to 
check the existence of the target element. 
This is the simplest way to check the 
existence of the element in the list.
"""
list=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
	data=int(input("Enter elements in the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
element=int(input("Enter element which is found to exist in list: "))
for i in list:
	if i==element:
		print("element exists using loop")

print("-------------METHOD 2 using in --------------------")
list=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
	data=int(input("Enter elements in the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
element=int(input("Enter element which is found to exist in list: "))
if element in list:
	print("element exists using in")
else:
	print("element doesnot exist")

print("----------------METHOD 3 using set()+in -------------- ")
#using set()+in
"""
Converting the list into set and then using in can possibly be more efficient than only using in.
But having efficiency for a plus also has certain negatives.
One among them is that the order of list is not preserved, 
and if you opt to take a new list for it, you would require to use extra space. 
Other drawback is that set disallows duplicacy and hence duplicate elements would be removed from the original list.
"""
from bisect import bisect_left
bisect_list=list=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
	data=int(input("Enter elements in the list: "))
	list.append(data)
print(f"elements in the list are: {list}")
element=int(input("Enter element whose existence is to be found: "))
list_set=set(list)
if element in list:
	print("element exists by using set()+in ")
bisect_list.sort()
if bisect_left(bisect_list,element):
	print("element exists by using sort()+bisect_left()")

