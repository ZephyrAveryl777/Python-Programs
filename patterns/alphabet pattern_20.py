'''
Pattern:
Enter number of rows: 5
 A B C D E E F G H
   A B C D D E F
     A B C C D
       A B B
         A
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(row-1),end=' ')
	for column in range(1,number_rows+2-row):
		print(chr(64+column),end=' ')
	for column in range(2,number_rows+2-row):
		print(chr(68+column-row),end=' ')
	print()