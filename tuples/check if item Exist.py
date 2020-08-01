'''
You can verify if a specified item 
is exists in a tuple using in keyword:
'''
test=[]
n=int(input('Enter size of tuple: '))
for i in range(n):
	data=input(f'Elements of tuple are: ')
	test.append(data)
test=tuple(test)
print(f'Elements of the tuple are: {test}')
if "israel" in test:
	print('yes')
else:
	print('False')