'''
Pattern:
Enter number of rows: 5
1
21
123
4321
12345
''' 
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	if row%2!=0:
		for column in range(1,row+1):
			print(column,end=' ')
	else:
		for column in range(row,0,-1):
			print(column,end=' ')
	print()