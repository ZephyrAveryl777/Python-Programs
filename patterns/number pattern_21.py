'''
Pattern
Enter number of rows: 5
12345
2345
345
45
5
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(row,number_rows+1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()