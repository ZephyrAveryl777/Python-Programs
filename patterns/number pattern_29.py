'''
Pattern
Enter number of rows: 5
56789
4567
345
23
1
'''
print('Number Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows-1,-1,-1):
	k=row
	for column in range(0,row+1):
		k+=1
		if  k<10:
			print(f'0{k}',end=' ')
		else:
			print(k,end=' ')
	print()
