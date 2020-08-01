'''
Pattern:
Enter number of rows: 5
E
D D
C C C
B B B B
A A A A A
B B B B
C C C
D D
E 
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print(chr(65+number_rows-row),end=' ')
	print()
for row in range(1,number_rows+1):
	for column in range(0,number_rows-row):
		print(chr(65+row),end=' ')
	print()