'''
Pattern:
Enter number of rows: 5
1
2  6
3  7  10
4  8  11 13
5  9  12 14 15
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	d=number_rows-1
	k=row
	for column in range(1,row+1):
		print('%-3d'%k,end=' ')
		k+=d
		d-=1
	print()