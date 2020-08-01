'''
Pattern
Enter number of rows: 5
1        1
12      21
123    321
1234  4321
1234554321
'''
print('Number Pattern: ')
number_rows=int(input('ENter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print( column,end=' ')
	for column in range(row*2,number_rows*2):
		print(' ',end=' ')
	for column in range(row,0,-1):
		print( column,end=' ')
	print()