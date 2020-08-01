'''
Pattern 
Enter number of rows: 5
1
22
333
2222
11111
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for columnn in range(1,row+1):
		if row<=number_rows//2:
			print('%-2d'%row,end=' ')
		else:
			print('%-2d'%(number_rows-row+1),end=' ')
	print()