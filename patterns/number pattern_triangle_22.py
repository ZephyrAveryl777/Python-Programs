'''
Pattern: 
Enter number of rows: 5
1
12
123
1234
12345
1234
123
12
1  
'''
print('Number of patterns: ')
number_rows=int(input('Enter number of rows: '))
#upper part of the pattern
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print('%-2d'%column,end='')
	print()
#lowe part of the pattern
for row in range(number_rows-1,0,-1):
	for column in range(1,row+1):
		print('%-2d'%column,end='')
	print()
