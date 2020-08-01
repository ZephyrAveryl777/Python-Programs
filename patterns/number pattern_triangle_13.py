'''
Pattern
Enter number of rows: 5
1
3 2
4 5 4 3
5 6 7 6 5 4
6 7 8 9 8 7 6 5
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(0,number_rows+1):
	k=row+1
	for column in range(3,row+1):
		print(k,end=' ')
		k+=1
	for column in range(((2*row)-1),row-1,-1):
		print(column,end=' ')
	print()