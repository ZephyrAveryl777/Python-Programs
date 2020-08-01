'''
Pattern:
Enter number of rows: 5
 E E E E E E E E E
   D D D D D D D
     C C C C C
       B B B
         A
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print('  '*(row-1),end=' ')
	for column in range(1,number_rows+2-row):
		print(chr(65+number_rows-row),end=' ')
	for column in range(2,number_rows+2-row):
		print(chr(65+number_rows-row),end=' ')
	print()