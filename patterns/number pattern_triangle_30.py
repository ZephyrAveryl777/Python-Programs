'''
Pattern
Enter number of rows: 5















'''
print('Number pattern: ')
number_rows=int(input('ENter number of rows: '))
print('*',end=' ')
for row in range(1,number_rows+1):
	print('*',end=' ')
	for column in range(1,row+1):
		print(column,end='')
	for column in range(row-1,0,-1):
		print(column,end='')
	print('*',end=' ')
	print()
for row in range(number_rows-1,0,-1):
	print('*',end=' ')
	for column in range(1,row+1):
		print(column,end='')
	for column in range(row-1,0,-1):
		print(column,end='')
	print('*',end=' ')
	print()
	print('*',end=' ')