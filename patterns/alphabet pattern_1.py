'''
Pattern
Enter number of rows: 5
A
BB
CCC
DDDD
EEEEE
'''
print('Alphabet pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print(chr(64+row),end=' ')
	print()