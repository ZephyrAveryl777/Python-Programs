'''
Pattern
Enter number of rows: 5
Enter number of columns: 5
54321
43212
32123
21234
12345
'''
print('Pattern: ')
number_rows=int(input('Enter number of rows: '))
print('',end='')
for row in range(1,number_rows+1):
	for column in range(((number_rows-row)+1),1,-1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')
	for column in range(1,row+1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')
	print()