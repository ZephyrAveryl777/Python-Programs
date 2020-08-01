'''
You can iterate tuple items by using
a for loop and in keyword.
'''
test=[]
n=int(input('Enter size of tuple: '))
for i in range(n):
	data=input('Enter elements of tuple: ')
	test.append(data)
test =tuple(test)
print(f'\nElements of tuple: {test}')
for item in test:
	print(f'Elements of tuple are: {item}')
