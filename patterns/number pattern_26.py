'''
Pattern
Enter number of rows: 5
    1
   23
  345
 4567
56789
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	k=row
	for column in range(row,number_rows+1):
		print('  ',end=' ')
	for column in range(1,row+1):
		k=k+1
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()