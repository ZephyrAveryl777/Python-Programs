'''
Pattern 
mirrored triangular rowise incremental number pattern
Enter number of rows: 5
    1
   22
  333
 4444
55555
'''
print('mirrored triangular rowise incremental number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(row,number_rows):
		print('  ',end=' ')
	for column in range(1,row+1):
		if row < 10:
			print(f'0{row}',end=' ')
		else: 
			print(row,end=' ')
	print()
