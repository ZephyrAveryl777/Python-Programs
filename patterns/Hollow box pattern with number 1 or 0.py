'''
Pattern 
box pattern with number 1 or 0:
Enter number of rows: 5
Enter number of columns: 5
11111
1   1
1   1
1   1
11111
'''
print('Box pattern with number 1 or 0:')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns:'))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if row==1 or row==number_rows or column==1 or column==number_columns:
			print('1',end='')
		else:
			print(' ',end='')
	print('\n',end='')