'''
Pattern
Enter number of rows: 5
1
21
321
4321
54321
'''
print('Number Pattern:')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(row,0,-1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()