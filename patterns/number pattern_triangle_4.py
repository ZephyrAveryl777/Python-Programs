'''
Pattern
Enter number of rows: 5
1
11
101
1001
11111
'''
print('Number triangle pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		if row==1  or row==number_rows or column==1 or column==row:
			print('1',end=' ')
		else:
			print('0',end=' ')
	print()