'''
To access tuple item need to refer it by it's the index number, 
inside square brackets:
'''
a=[]
n=int(input('Enter size of tuple: '))
for i in range(n):
	data=input('Enter elements of tuple: ')
	a.append(data)
tuple_a=tuple(a)
print(f'Tuple elements: {tuple_a}')

for i in range(n):
	print(f'\nElements of tuple at position {i+1} is: {tuple_a[i]}')