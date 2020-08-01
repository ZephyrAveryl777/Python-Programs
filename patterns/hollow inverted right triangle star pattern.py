'''
Pattern 
Hollow inverted right triangle star pattern
Enter number of rows: 5
*****
*  *
* *
**
*
'''
print('Hollow inverted right triangle star pattern: ')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(i,rows+1):
		if i==1 or i==j or j==rows:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print('\n',end='')