'''
Pattern
Enter number of rows: 5
1
01
010
1010
10101
'''
print('Pattern: ')
number_rows=int(input('ENter number of rows: '))
k=1
for row in range(1,number_rows+1):
	for columnn in range(1,row+1):
		if k%2 ==1:
			print('1',end=' ')
		else:
			print('0',end=' ')
		k+=1
	print()