'''
Pattern
Downward Arrow Star Pattern:
Enter number of rows: 5
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
'''
print('Downward Arrow Star Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(0,number_rows):
	for column in range(row+1):
		print('*',end=' ')
	for column in range(2*(number_rows-row-1)):
		print(' ',end=' ')
	for column in range(row+1):
		print('*',end=' ')
	print()