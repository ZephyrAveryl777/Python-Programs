'''
Pattern
1, 0 at alternate columns
Enter number of rows: 5
Enter number of column: 5
01010
01010
01010
01010
01010
'''
print('1,0 at alternate column: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of column: '))
for row in range(1,row+1):
	for column in range(1,column+1):
		if column%2==1:
			print('0',end='')
		else:
			print('1',end='')
	print('\n',end='')
