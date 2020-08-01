'''
Pattern
Enter number of rows: 5
1
23
345
4567
56789
'''
print('number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(0,number_rows+1):
	k=row
	for column in range(1,row+2):
		k=k+1
		if k < 10:
			print(f'0{k}',end=' ')
		else:
			print(k,end=' ')
	print()