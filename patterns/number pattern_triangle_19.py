'''
Pattern:
Enter number of rows: 5
1
3  2
4  5  6
10 9  8  7
11 12 13 14 15
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
counter=0
for row in range(1,number_rows+1):
	k=counter+1 if row%2!=0 else counter+row
	for column in range(1,row+1):
		print('%-3d'%k,end=' ')
		if row%2!=0:
			k+=1
		else:
			k-=1
		counter+=1
	print()
