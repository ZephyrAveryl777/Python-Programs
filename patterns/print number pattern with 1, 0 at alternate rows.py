'''
Pattern
1,0 at alternate rows:
Enter number of rows: 5
Enter number of column: 5 
10101
10101
10101
10101
10101
'''
print('1,0 at alternate rows: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if column%2==1:
			print('1',end='')
		else:
			print('0',end='')
	print('\n',end='')