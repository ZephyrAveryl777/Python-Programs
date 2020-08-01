'''
Pattern 
Hollow inverted pyramid star pattern
Enter number of rows:
*********
 *     *
  *   *
   * *
    *
'''
print('Hollow inverted pyramid star pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows*2):
		if row==1 or row==column or row+column==number_rows*2:
			print('*',end="")
		else: 
			print(end=" ")
	print()