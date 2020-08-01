'''
Pattern 8
Right triangle star pattern
Enter number of rows: 5
*
**
***
****
*****
'''
print('Right triangle star pattern:')
rows=int(input('Enter number of rows:'))
for i in range(0,rows+1):
	for j in range(0,i):
		print('*',end=" ")
	print('\n',end='')
