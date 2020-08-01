"""
Example
Enter the number of rows: 5
E D C B A
E D C B
E D C
E D
E
"""
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows+2-row):
		print(chr(65+(number_rows-column)),end=' ')
	print()