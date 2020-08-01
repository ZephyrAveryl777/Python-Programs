print("-------METHOD 1-----------")
""""
Using Traversal
Initialize the value of product to 1
(not 0 as 0 multiplied with anything returns zero).
Traverse till the end of the list, multiply every 
number with the product. The value stored in the 
product at the end will give you your final answer.
"""
def multiplyList(list):
	#multiply elements one by one
	result = 1	
	for i in list:
		result=result*i
	return result

list=[]
n=int(input("Enter size of the lsit: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the lsit are: {list}")
print(f"product of all the elements of the list are:  {multiplyList(list)}")

print("-----------METHOD 2-----------------")
"""
We can use numpy.prod() from import numpy 
to get the multiplication of all the numbers 
in the list. It returns an integer or a float value
depending on the multiplication result.
"""
import numpy
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f'elements of the list are: {list}')
#using numpy.prod() to get the multiplication
result1=numpy.prod(list)
print(f'product of all elements of the list are: {result1}')

print("-----------METHOD 3-------------------")
#using lambda function
"""
Lambda definition does not include a “return” statement,
it always contains an expression which is returned. 
We can also put a lambda definition anywhere a function is expected, 
and we don’t have to assign it to a variable at all. 
This is the simplicity of lambda functions. 
The reduce() function in Python takes in a function and a list as 
argument. The function is called with a lambda function and 
a list and a new reduced result is returned. This performs a 
repetitive operation over the pairs of the list.
"""
from functools import reduce
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the list are: {list}")
result=reduce((lambda x,y:x*y),list)
print(f"product of all the elements of the list: {result}")

print("-------------METHOD 4----------------")
import math
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the list: {list}")
result=math.prod(list)
print(f"product of all the elements of the list:{result}")