'''
Pattern 6
Mirrored rhombus star
Enter number of rows: 5
*****
 *****
  *****
   *****
    *****
'''
print('Mirrored rhombus star pattern:')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(1, i):
		print(' ',end=' ')
	for j in range(1,rows+1):
		print('*',end=' ')
	print('\n',end=' ')

print('-------------------------------')
'''
mirrored parallelogram star pattern
Enter number of rows: 5
Enter number of columns: 10
********************
 ********************
  ********************
   ********************
    ********************
'''
print('Mirrored parallelogram star pattern: ')
rows=int(input('Enter number of rows: '))
columns=int(input('Enter number of columns: '))
for i in range(1,rows+1):
	for j in range(1,i):
		print(' ',end=' ')
	for j in range(1,columns+1):
		print('*',end=' ')
	print('\n',end=' ')
