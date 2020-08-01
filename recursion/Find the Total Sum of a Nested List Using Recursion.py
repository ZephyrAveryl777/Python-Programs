'''
Problem Description:
--------------------
The program takes a nested list 
and finds the total sum of the 
nested list using recursion.
'''
print(__doc__,end="")
print('-'*25)
def rsum(L):
    if type(L) != list:
        return L
    if L == []:
        return 0
    return rsum(L[0]) + rsum(L[1:])
lst=[]
n=int(input('Enter size of list: '))
for i in range(n):
	data=[int(input(f'Enter first sublist elements at position {i+1}: ')),
	int(input(f'Enter the elements of second sublist at position {i+1}: '))]
	lst.append(data)
print(f'Elements of the nested list: {lst} and sum of its elements is: {rsum(lst)}')
