'''
pattern
Enter number of rows: 5
1
00
111
0000
11111
'''
print('pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		if row%2==1:
			print('1',end=' ')
		else:
			print('0',end=' ')
	print()