'''
Pattern 9
Hollow mirrored right triangle
Enter number of rows: 5
    *
   **
  * *
 *  *
*****
'''
print('Hollow mirrored right triangle:')
rows=int(input('Enter number of rows:'))
for i in range(0,rows+1):
	for j in range(i,rows+1):
		print(' ',end='')
	for j in range(1,i+1):
		if i==rows or j==1 or j==i:
			print('*',end="")
		else:
			print(' ',end='')
	print('\n',end='')
