'''
Alphabet Pattern:
Enter number of rows: 5
     A
    CCC
   EEEEE
  GGGGGGG
 IIIIIIIII
'''
print('Alphabet Pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(number_rows-row),str(chr(64+2*row-1)+'')*(2*row-1))
	