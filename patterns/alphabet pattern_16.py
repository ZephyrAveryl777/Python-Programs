'''
Pattern:
Enter the number of rows: 5
         A
       A B A
     A B C A B
   A B C D A B C
 A B C D E A B C D
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(number_rows-row),end=' ')
	for column in range(1,row+1):
		print(chr(column+64),end=' ')
	for column in range(1,row):
		print(chr(64+column),end=' ')
	print()