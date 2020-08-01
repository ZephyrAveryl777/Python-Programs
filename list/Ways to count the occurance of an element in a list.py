print("-------------METHOD 1--------------")
#simple approach
"""
We keep a counter that keeps on increasing 
if the esquired element is found in the list.
"""
def countX(list,x):
	count=0
	for ele in list:
		if ele == x:
			count=count+1
	return count

list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements in the list: "))
	list.append(data)
print(f"elements in the list: {list}")
element=int(input("Enter the element whose occurance is to be found: "))
print(f"{element} has occurred {countX(list,element)} times.")

print("----------------METHOD 2------------------")
""" 
Using Counter()
Counter method returns a dictionary 
with occurrences of all elements as a key-value pair,
where key is the element and value is the number of times 
that element has occurred.
"""
from collections import Counter
list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements in the list: "))
	list.append(data)
print(f"elements in the list: {list}")
element=int(input("Enter the element whose occurance is to be found: "))
d=Counter(list)
print(f"{element} has occurred {d[element]} times.")


print("-------------METHOD 3---------------")
def countX(list,x):
	return list.count(x)
list=[]
n=int(input("Enter size of the list: "))
for i in range(n):
	data=int(input("Enter elements in the list: "))
	list.append(data)
print(f"elements in the list: {list}")
element=int(input("Enter the element whose occurance is to be found: "))
d=Counter(list)
print(f"{element} has occurred {countX(list,element)} times.")