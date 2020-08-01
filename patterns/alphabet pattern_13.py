'''
Pattern:
Enter number of rows: 5
     A
    A B C
   A B C D E
  A B C D E F G
 A B C D E F G H I
'''
print('Alphabet pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(number_rows-row),end=' ')
	for column in range(65,65+2*row-1):
		print(chr(column),end=' ')
	print()