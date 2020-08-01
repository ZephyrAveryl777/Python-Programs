'''
Pattern
Column increment number pattern:
Enter number of rows: 5
Enter number of columns: 5
12345
12345
12345
12345
12345
'''
print('column increment number pattern:')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		#print the current column number
		print(column,end='')
	print('\n',end='')