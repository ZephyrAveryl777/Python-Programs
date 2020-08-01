'''
Pattern:
Enter number of rows: 5
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows+1):
		print(chr(64+column),end=' ')
	print()
