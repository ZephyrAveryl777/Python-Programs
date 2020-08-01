"""
Example:
Enter the number of rows: 5
A A A A A
B B B B
C C C
D D
E
"""
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows+2-row):
		print(chr(64+row),end=' ')
	print()