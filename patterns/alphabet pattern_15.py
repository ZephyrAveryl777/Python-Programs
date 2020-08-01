'''
Pattern:
Enter number of rows: 5
         A
       B A B
     C B A B C
   D C B A B C D
 E D C B A B C D E
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in  range(1,number_rows+1):
	print(' '*(number_rows-row),end=' ')
	for column in range(1,row):
		print(chr(row-column+65),end=' ')
	for column in  range(0,row):
		print(chr(column+65),end=' ')
	print()