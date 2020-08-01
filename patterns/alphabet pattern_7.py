"""
Example:
Enter the no of rows: 5
     A

    B B

   C C C

  D D D D

 E E E E E
"""
print('Alphabet pattern:  ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(number_rows-row),(chr(64+row)+' ')*row)
	print()