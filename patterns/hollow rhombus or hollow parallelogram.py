'''
Pattern 5
Hollow Rhombus Star
   *****
  *   *
 *   *
*   *
*****
'''
print('Hollow Rhombus Star: ')
rows=int(input('Enter number of rows: '))
for i in range(1,rows+1):
	for j in range(0,rows-i):
		print('  ',end=" ")
	for j in range(1,rows+1):
		if i==1 or i==rows or j==1 or j==rows:
			print('*',end=" ")
		else:
			print(' ',end=" ")
	print('\n',end=" ")

print('------------------------------------')
'''
Parallelogram star pattern
Enter rows: 5 
Enter columns: 10
     **********
    *        *
   *        *
  *        *
 **********
'''
print('Parallelogram star pattern: ')
rows=int(input('Enter number of rows: '))
columns=int(input('Enter number of columns: '))
for i in range(1,rows+1):
	for j in range(0,rows-i):
		print(' ',end=' ')
	for j in range(1,columns+1):
		if i==1 or i==rows or j==1 or j==columns:
			print('*',end=" ")
		else:
			print(' ',end=" ")
	print('\n',end=' ')