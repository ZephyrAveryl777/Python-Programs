'''
Problem Description:
-------------------
The program takes a 
nested list and flattens 
it using recursion.
'''
print(__doc__,end="")
print('-'*25)
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
s=[]
n=int(input('Enter size of list: '))
for i in range(n):
	data=[int(input(f'Enter first sublist elements (only interges) at position {i+1}: ')),
	input(f'Enter the elements of second sublist (only charcters) at position {i+1} : ')]
	s.append(data)
print(f'Elements of the nested list: {s}')
print(f"Flattened list is: {flatten(s)}")