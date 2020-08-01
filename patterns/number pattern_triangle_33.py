'''
Pattern
Enter number of rows: 5
1
2  3
4  5  6
7  8  9  10
11 12 13 14 15
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
k=1
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print(k,end=' ')
		k+=1
	print()