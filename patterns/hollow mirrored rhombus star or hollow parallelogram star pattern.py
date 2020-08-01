'''
Pattern 7
Hollow mirrored rhombus star pattern
Enter number of rows: 5
*****
 *   *
  *   *
   *   *
    *****
'''
print('Hollow mirrored rhombus star pattern:')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(1,i):
		print(' ',end=" ")
	for j in range(1,rows+1):
		if i==1 or i==rows or j==1 or j==rows:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print('\n',end=' ')

print('---------------------------------------')
'''
Hollow mirrored parallelogram star pattern
Enter number of rows: 5
Enter number of columns: 10
********************
 *                  *
  *                  *
   *                  *
    ********************
'''
print('Hollow mirrored parallelogram star pattern:')
rows=int(input('Enter number of rows: '))
columns=int(input('Enter number of columns: '))
for i in range(1,rows+1):
	for j in range(1,i):
		print(' ',end=' ')
	for j in range(1,columns+1):
		if i==1 or i==rows or j==1 or j==columns:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print('\n',end=' ')
	