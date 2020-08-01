'''
Pattern 
Hollow mirrored half diamond star pattern
Enter number of rows: 5
        * 
      * * 
    *   * 
  *     * 
*       * 
  *     * 
    *   * 
      * * 
        * 
'''
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows*2):
	for column in range(1,number_rows+1):
		if column==number_rows or row+column==number_rows+1 or row-column==number_rows-1:
			print('*',end=' ')
		else: 
			print(' ',end=' ')
	print('\n',end='')