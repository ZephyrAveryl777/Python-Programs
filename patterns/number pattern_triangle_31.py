'''
Enter number of rows: 5
1       1
 2     2
  3   3
   4 4
    5
   4 4
  3   3
 2     2
1       1
'''
print('Cross number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row):
		print(' ',end=' ')
	print('%-2d'%row,end=' ')
	for column in range(1,(number_rows-row)*2):
		print(' ',end=' ')
	if row!=number_rows:
		print('%-2d'%row,end=' ')
	print()
for row in range(number_rows-1,0,-1):
	for column in range(1,row):
		print(' ',end=' ')
	print(row,end=' ')
	for column in range(1,(number_rows-row)*2):
		print(' ',end=' ')
	print('%-2d'%row,end=' ')
	print()