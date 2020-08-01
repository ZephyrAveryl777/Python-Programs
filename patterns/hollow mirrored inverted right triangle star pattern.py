'''
Pattern 
Hollow mirrored inverted right triangle star pattern
Enter number of rows: 5
*****
 *  *
  * *
   **
    *
'''
print('Hollow mirrored inverted right triangle star pattern: ')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(1,i):
		print(' ',end='')
	for j in range(i,rows+1):
		if j==i or j==rows or i==1:
			print('*',end='')
		else:
			print(' ',end='')
	print('\n',end='')