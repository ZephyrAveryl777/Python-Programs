'''
Pattern
box number pattern with plus in center
Enter number of rows: 5
Enter number of columns: 5
11011
11011
00000
11011
11011
'''
print('box number pattern with plus in center: ')
number_rows=int(input('Enter number or rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if ((number_columns+1)//2)==column or ((number_rows+1)//2)==row:
			print('0',end='')
		elif ((number_columns%2==0 and (((number_columns+1)//2)+1)==column)) or (number_rows%2==0 and (((number_rows+1)//2)+1)==row):
			print('0',end='')
		else:
			print('1',end='')
	print('\n',end='')
