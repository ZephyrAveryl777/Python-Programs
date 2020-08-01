'''
Pattern 
Hollow half daimond star pattern
Enter number of rows: 5
*    
**   
* *  
*  * 
*   *
*  * 
* *  
**   
* 
'''
print('Hollow half diamond star pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows*2):
	for column in range(1,number_rows+1):
		if column==1 or row==column:
			print('*',end='')
		elif row+column==number_rows*2:
			print('*',end='')
		else:
			print(' ',end='')
	print('\n',end='')