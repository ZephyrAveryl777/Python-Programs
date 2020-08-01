'''
Pattern 
Number sequence in rows:
Enter number of rows: 5
Enter number of column: 5
12345
23456
34567
45678
56789
'''
print('Number sequence in rows:')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(row,row+number_columns):
		print(column,end='')
	print('\n',end='')
