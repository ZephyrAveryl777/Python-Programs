'''
Pattern
Enter number of rows: 5
12345
1234
123
12
1
'''
print('pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows-row+2):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()