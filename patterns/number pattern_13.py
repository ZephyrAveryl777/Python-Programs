'''
Pattern
Enter number of rows: 5
54321
4321
321
21
1
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows,0,-1):
	for column in range(row,0,-1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()