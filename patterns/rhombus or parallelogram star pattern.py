'''
Pattern 4
Enter rows: 5
Rhombus star pattern
     *****
    *****
   *****
  *****
 *****
'''
print('rhombus star pattern:')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(0,rows-i):
		print(' ',end=" ")
	for j in range(1,rows+1):
		print('*',end=" ")
	print('\n',end=' ')

print('------------------------------------')
'''
Pattern 4
Parallelogram star pattern
Enter rows: 5
Enter column: 10
    ************
   ************
  ************
 ************
************
'''
print('Parallelogram star pattern')
rows=int(input('enter number of rows: '))
columns=int(input('Enter number of columns: '))
for i in range(1,rows+1):
	for j in range(0,rows-i):
		print(' ',end=" ")
	for j in range(1,columns+1):
		print('*',end=' ')
	print('\n',end=" ")
