'''






'''
#number_rows=int(input('Enter number of rows: '))
for row in range(8):
	for column in range(9):
		if ((row==0 and column%(4)!=0) or (row==1 and column%(4)==0) or (row-column==2) or (row+column==10)):
			print('*',end='')
		else:
			print(' ',end='')
	print('\n',end='')