'''
Pattern 
Hollow pyramid star pattern
Enter number of number_rows: 5
    *
   * *
  *   *
 *     *
*********
'''
print('Hollow pyramid star pattern: ')
#the naming is done in a simplified way so as to avoid any confusion.
'''
number of rows: number_rows
i=row
j=column
'''
number_rows=int(input('Enter number of number_rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows*2):
		if row==number_rows or row+column==number_rows +1 or column-row==number_rows-1:
			print('*',end='')
		else:
			print(end=" ")
	print()


print('--------------------------------------------')
'''
    *
   * *
  *   *
 *     *
* * * * *
'''
print('Hollow pyramid star pattern with no stars at even position in the base: ')
number_rows=int(input('Enter number of number_rows: '))
k=2
for row in range(1,number_rows+1):
	for column in range(1,number_rows*2):
		if row+column==number_rows+1 or column-row==number_rows-1:
			print('*',end='')
		elif row==number_rows and column!=k:
			print('*',end='')
			k=k+2
		else:
			print(end=' ')
	print()