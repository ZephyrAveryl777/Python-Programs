'''
Pattern
Plus star pattern:
Enter number of rows: 5
    +
    +
    +
    +
+++++++++
    +
    +
    +
    +
'''
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows+1):
		if number_rows%2!=0:
			if row==((number_rows//2)+1) or column==((number_rows//2)+1) :
				print('*',end=" ")
			else:
				print(' ',end=' ')
		else:
			if row==(((number_rows+1)//2)+1) or column==(((number_rows+1)//2)+1) :
				print('*',end=" ")
			else:
				print(' ',end=' ')
	print('\n',end='')
		#print(f'Row=> {row}, column=> {column}')