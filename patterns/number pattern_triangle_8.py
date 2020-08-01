'''
Pattern:
Enter number of rows: 5
1
131
13531
1357531
135797531
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,(2*row-1)+1,2):
		if column<10: 
			print(f' {column}',end=' ')
		else:
			print(column,end=' ')
	for column in range((row-1)*2-1,0,-2):
		if column<10: 
			print(f' {column}',end=' ')
		else:
			print(column,end=' ')
	print()