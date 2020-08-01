'''
Pattern 
print circle box number pattern with 1 and 0
Enter number of rows: 5
Enter number of columns: 5
01110
10001
10001
10001
01110
'''
print('print circle box number pattern with 1 and 0: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		#print corner elements
		if (row==1 or row==number_rows) and (column==1 or column==number_columns):
			print('0',end='')
		elif row==1 or row==number_rows or column==1 or column==number_columns:
			print('1',end='')
		else:
			print('0',end='')
	print('\n',end='')