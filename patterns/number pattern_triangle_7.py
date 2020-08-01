'''
Pattern
Enter number of rows: 5
1
24
135
2468
13579
'''
print('Number pattern: ')
number_row=int(input('ENter number of rows: '))
for row in range(1,number_row+1):
	if row%2!=0:
		k=1
	else:
		k=2
	for column in range(1,row+1):
		print(k,end=' ')
		k+=2

	print()