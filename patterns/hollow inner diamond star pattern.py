'''
Pattern
Inner hollow diamond star pattern
Enter number of rows: 5
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
'''
print('Inner Hollow Diamond star pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows,0,-1):
	for column in range(row,0,-1):
		print('*',end=' ')
	for column in range(2*(number_rows-row)):
		print(' ',end=' ')
	for column in range(row,0,-1):
		print('*',end=' ')
	print()
for row in range(1,number_rows):
	for column in range(row+1):
		print('*',end=' ')
	for column in range(2*(number_rows-row-1)):
		print(' ',end=' ')
	for column in range(row+1):
		print('*',end=' ')
	print()