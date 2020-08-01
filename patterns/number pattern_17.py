'''
Pattern 
Enter number of rows: 5
54321
5432
543
54
5
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(number_rows,row,-1):
		if column < 10:
			print(f'0{column}',end=' ')
		else: 
			print(column,end=' ')
	print()