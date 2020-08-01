'''
Problem Description
-------------------
The program takes a list and finds the 
sum of elements in a list recursively.
'''
print(__doc__,end='')
print('-'*25)
def sum_arr(arr,size):
   if (size == 0):
     return 0
   else:
     return arr[size-1] + sum_arr(arr,size-1)
n=int(input("Enter the number of elements for list: "))
a=[]
for i in range(0,n):
    element=int(input("Enter element: "))
    a.append(element)
print(f"Element of list are : {a}")
print(f"Sum of items in list {a} is: {sum_arr(a,n)}")
