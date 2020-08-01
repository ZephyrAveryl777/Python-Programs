'''
Pattern 
Cross star pattern:
Enter number of rows: 5
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
'''
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows+1):
		if row==column or row+column==number_rows+1:
			print('*',end='')
		else: 
			print(' ',end='')
	print()