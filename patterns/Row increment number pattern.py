'''
Pattern
Row increment number pattern:
Enter number of rows: 5
Enter number of columns: 5
11111
22222
33333
44444
55555
'''
print('Row increment number pattern: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns:'))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		#print the current row number
		print(row,end='')
	print('\n',end='')