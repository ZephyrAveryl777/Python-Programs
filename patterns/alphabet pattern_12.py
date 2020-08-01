'''
Alphabet Pattern:
Enter number of rows: 5
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows+1):
		print(chr(64+row),end=' ')
	print()