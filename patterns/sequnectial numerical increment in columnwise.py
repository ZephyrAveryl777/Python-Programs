'''
Pattern
sequnectial numerical increment in columnwise
Enter number of rows: 5
Enter number of columns: 5
1  2  3  4  5
6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
print('sequnectial number increment in columnwise: ')
number_rows=int(input('Enter number of rows: '))
number_columns=int(input('Enter number of columns: '))
k=0
for row in range(1,number_rows+1):
	for column in range(1,number_columns+1):
		k=k+1
		print('%-3d'%k,end='')
	print('\n',end='')

