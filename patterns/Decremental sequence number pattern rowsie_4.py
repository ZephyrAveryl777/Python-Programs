'''
Pattern 
decremental sequance number pattern 
Enter number of rows: 5
Enter number of columns: 5
12345
22345
33345
44445
55555
'''
print('decremental sequance number pattern: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
for row in range(1,number_rows+1):
	for column in range(0,row-1):
		if row <10:
			print(' ',end='')
			print(row,end=' ')
		else: 
			print(row,end=' ')
	for column in range(row,number_columns+1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')
	print()
