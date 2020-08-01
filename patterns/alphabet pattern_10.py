'''
Alphabet Pattern:
Enter number of rows: 5
 ABCDE
  ABCD
   ABC
    AB
     A
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(row-1),end=' ')
	for column in range(65,66+number_rows-row):
		print(chr(column),end=' ')
	print()