'''
Pattern
Enter number of rows: 5
5
45
345
2345
12345
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows,0,-1):
	for column in range(row,number_rows+1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()