'''
Pattern 
Enter number of rows: 5
13579
3579
579
79
9
'''
print('Pattern: ')
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(0,number_rows):
	k=(row*2)-1
	for column in range(row,number_rows):
		k+=2
		if k < 10: 
			print(f'0{k}',end=' ')
		else:
			print(k,end=' ')
	print()