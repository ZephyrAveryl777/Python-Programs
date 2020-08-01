'''
Pattern
Enter number of rows: 5
1
2 3
4 5 6 7
8 9 1 2 3 4 5 6
7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4
'''
print('Number pattern: ')
counter=1
k=1
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,counter+1):
		if k==10:
			k=1
		print(k,end=' ')
		k+=1
	print()
	counter*=2
