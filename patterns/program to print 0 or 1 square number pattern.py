'''
Pattern
Square number pattern:
Enter number of rows: 5
Enter number of column: 5
11111
11111
11111
11111
11111
'''
print('Square number pattern: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns:'))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		print('1',end='')
	print('\n',end='')
