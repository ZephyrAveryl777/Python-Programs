'''
pattern:
cross number pattern with digit 1:
Enter number of rows: 5
Enter number of columns: 5
1   1
 1 1 
  1  
 1 1 
1   1
'''
print('box number pattern of 1 and 0 with cross center: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('ENter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if row==column or column==((number_columns+1)-row):
			print('1',end='')
		else:
			print(' ',end='')
	print('\n',end='')