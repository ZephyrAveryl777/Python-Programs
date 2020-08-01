'''
Pattern
Enter number of rows: 5
5
54
543
5432
54321
'''
print('Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows,0,-1):
	for column in range(number_rows,row-1,-1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()
