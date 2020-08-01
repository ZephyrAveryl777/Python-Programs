'''
Pattern
print chessboard number pattern with 1 and 0
Enter number of rows: 5
Enter number of columns: 5
10101
01010
10101
01010
10101
'''
print('print chessboard number pattern with 1 and 0 (Just use odd numbers for input):')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns:'))
k=1
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if k==1:
			print('1',end='')
		else:
			print('0',end='')
		k *= -1
		if number_columns%2==0:
			k *= -1
	print('\n',end='')
