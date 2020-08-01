'''
Pattern 
Half Diamond Star Pattern
Enter number of rows:5
*
**
***
****
*****
****
***
**
*
'''
print('Half Diamond Star Pattern')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row+1):
		print('*',end='')
	print()
for row in range(number_rows-1,0,-1):
	for column in range(0,row):
		print('*',end='')
	print()