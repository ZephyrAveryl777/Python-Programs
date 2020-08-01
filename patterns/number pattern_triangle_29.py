'''
Pattern
Enter number of rows: 5
1
121
12321
1234321
123454321
1234321
12321
121
1   
'''
print('Number pattern: ')
number_rows=int(input('ENter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print(column,end='')
	for column in range(row-1,0,-1):
		print(column,end='')
	print()
for row in range(number_rows-1,0,-1):
	for column in range(1,row+1):
		print(column,end='')
	for column in range(row-1,0,-1):
		print(column,end='')
	print()