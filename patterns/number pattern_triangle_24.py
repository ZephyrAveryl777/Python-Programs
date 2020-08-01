'''
Pattern
Enter number of rows: 5
            1 
         1 2 
      1 2 3 
   1 2 3 4 
1 2 3 4 5 
   1 2 3 4 
      1 2 3 
         1 2 
            1 
'''
print('Number of patterns: ')
number_rows=int(input('Enter number of rows: '))
#upper part of the pattern
for row in range(1,number_rows+1):
	for column in range(number_rows-1,row-1,-1):
		print('  ',end=' ')
	for column in range(1,row+1):
		print(column,end=' ')
	print()
#lowe part of the pattern
for row in range(number_rows-1,0,-1):
	for column in range(row,number_rows):
		print('  ',end=' ')
	for column in range(1,row+1):
		print(column,end=' ')
	print()
