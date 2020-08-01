'''
Pattern
box number pattern of 1 with 0 center
Enter number of row: 5
Enter number of column: 5
11111
11111
11011
11111
11111
'''
print('box number of 1 with 0 at center: ')
print('Note! just enter odd numbers as input! to avoid complications as of now.')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if column==((number_columns+1)//2) and row==((number_rows+1)//2):
			print('0',end='')
		elif number_columns%2==0 and (((number_columns+1)//2)+1)==column:
				if ((number_rows+1)//2)==row or (number_rows%2==0 and (((number_rows+1)//2)+1)==row):
					print('0',end='')
				else:
					print('1',end='')
		elif number_rows%2==0 and (((number_rows+1)//2)+1)==row:
			if (number_columns+1)//2 ==column or (number_columns%2==0 and (((number_columns+1)//2)+1)==column):
					print('0',end='')
		else: print('1',end='')
    
	print('\n',end='')

