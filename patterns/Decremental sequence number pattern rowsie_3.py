'''
Pattern
Decremental sequence number pattern_3
Enter number of rows: 5
Enter number of columns: 5
54321
54322
54333
54444
'''
print('Decremental sequence number pattern_3:')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
print('',end='')
for row in range(1,number_rows+1):
	for column in range(number_columns,row,-1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')

	for column in range(0,row):
		if row <10:
			print(' ',end='')
			print(row,end=' ')
		else: 
			print(row,end=' ')
	print()