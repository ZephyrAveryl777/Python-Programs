'''
Pattern 3 (hollow square with diagonal)
Enter number of rows: 5
*****
** **
* * *
** **
*****
''' 
print('Hollow Square with diagonal: ')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(1,rows+1):
		if i==1 or i==rows or j==1 or j==i or j==rows-i+1 or j==rows:
			print('*',end=" ")
		else:
			print(' ',end=' ')
	print('\n')