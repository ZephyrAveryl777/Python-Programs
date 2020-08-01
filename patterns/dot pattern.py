print('print chessboard number pattern with 1 and 0 (Just use odd numbers for input):')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns:'))
k=1
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		if k==1:
			print('(',end='')
		else:
			print('_)',end='')
		k *= -1
		if number_columns%2==0:
			k *= -1
	print('\n',end='')
