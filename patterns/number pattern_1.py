'''
Pattern 
Enter number of rows: 5
Enter number of column: 5
12345
21234
32123
43212
54321
'''
print('Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(row,1,-1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')
	for column in range(1,((number_rows-row)+1)+1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')
	print()
