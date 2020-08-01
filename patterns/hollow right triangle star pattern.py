'''
Pattern 9
Hollow right triangle star:
Enter number of rows: 5
*
**
* *
*  *
*****
'''
print('Hollow right triangle star: ')
rows=int(input('Enter number of rows: '))
for i in range(0,rows+1):
	for j in range(1,i+1):
		if j==1 or j==i or i==rows:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print('\n',end=' ')
