'''
pattern 
Enter number of rows: 5
54321
 4321
  321
   21
    1
'''
print('pattern: ')
number_row=int(input('Enter number of rows: '))
for row in range(number_row,0,-1):
	for column in range(row,number_row):
		print('  ',end=' ')
	for column in range(row,0,-1):
		if column < 10:
			print(f'0{column}',end=' ')
		else:
			print(column,end=' ')
	print()