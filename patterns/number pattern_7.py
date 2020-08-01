'''
Pattern
Enter number of rows:
1
12
123
1234
12345
'''
print('Pattern: ')
number_row=int(input('Enter number of rows: '))
for row in range(1,number_row+1):
	for column in range(1,row+1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()