'''
Pattern 
reverse Pyramid star pattern
Enter number of rows: 5
*********
 *******
  *****
   ***
    *
''' 
print('Reverse Pyramid star: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,row):
		print(' ',end='')
	for column in range(2*number_rows,2*row-1,-1):
		print('*',end='')
	print()

