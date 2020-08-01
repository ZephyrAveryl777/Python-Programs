'''
Pattern 
Decremental sequence number pattern rowise  to left
Enter number of rows: 5
Enter number of columns : 5
5 5 5 5 5 
4 4 4 4 5 
3 3 3 4 5 
2 2 3 4 5 
1 2 3 4 5 
'''
print('Decremental sequence number pattern rowise to left')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
print('',end='')
for row in range(number_rows,0,-1):
	for column in range(0,row):
		if row <10:
			print(' ',end='')
			print(row,end=' ')
		else: 
			print(row,end=' ')
	for column in range(row,number_columns+1):
		if column < 10:
			print(' ',end='')
			print(column,end=' ')
		else: 
			print(column,end=' ')
	print('\n',end='')