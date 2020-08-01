#naive method
print("----------METHOD 1--------------------------")
list=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
	data=int(input("Enter elements of the array: "))
	list.append(data)
print(f"elements in the list: {list}",end=" ")
# for i in range(n):
# 	print(list[i],end=" ")
print()
counter=0
for i in list:
	counter=counter+1
print(f"Length of list using navie method is: {counter}")

print("---------------------METHOD 2-----------------------")
"""
using len() method
The len() method offers the most used and easy way to find length of any list. 
This is the most conventional technique adopted by all the programmers today.
"""
a=[]
a.append("Hello")
a.append("How")
a.append("are")
a.append("you")
a.append("?")
print(f"The length of list {a} is: {len(a)}")

print("------------------METHOD 3------------------------")
"""
Using length_hint()
This technique is lesser known technique of finding list length. 
This particular method is defined in operator class and it can also tell
the no. of elements present in the list.
"""
from operator import length_hint
list=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"The list is: {list}")
#Finding length of list using len()
list_len=len(list)
#Find length of list using length_hint()
list_len_hint=length_hint(list)
#print length of list 
print(f"Length of list using len() is : {list_len}")
print(f"length of list using length_hint() is: {list_len_hint}")
