'''
Pattern
Enter number of rows: 5
1
2  4
7  11 16
22 29 37 46
56 67 79 92 106
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
sum=1;k=1
#counter=0
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print('%-3d'%sum,end=' ')
		sum+=(k)
		k+=1
	print()