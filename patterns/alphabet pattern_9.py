"""
Pattern: 
Enter the number of rows: 5
 EEEEE
  DDDD
   CCC
    BB
     A
"""
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(row-1),str(chr(65+(number_rows-row))+'')*(number_rows+1-row))