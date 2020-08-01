'''
Pattern 
Enter number of rows: 5
Enter number of columns: 5
12345
23451
34521
45321
54321
'''
print('Pattern:')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(row,number_columns+1):
		print(column,end=' ')
	for column in range(row-1,0,-1):
		print(column,end=' ')
	print()