'''
Pattern 
Diamond star pattern
Enter number of rows: 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''
print('Diamond Star Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(number_rows): 
	print(' '*(number_rows-row-1)+'* '*(row+1))
for row in range(number_rows-1):
	print(' '*(row+1)+'* '*(number_rows-row-1) )