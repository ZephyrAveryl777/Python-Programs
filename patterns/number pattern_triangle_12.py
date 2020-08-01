'''
Pattern:
Enter number of rows: 5
1
121
12321
1234321
123454321
'''
print('Number triangle pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		if column < 10:
			print(column,end=' ')
		else: 
			print(column,end=' ')
	for column in range(row-1,0,-1):
		if column<10: 
			print(column,end=' ')
		else:
			print(column,end=' ')
	print()