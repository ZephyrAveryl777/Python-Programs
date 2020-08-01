'''
Pattern
Mirrored Half Diamond Star Pattern
Enter number of rows: 5
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
print('Mirrored Half Diamond Star Pattern: ')
number_rows=int(input('enter number of rows: '))
for row in range(number_rows):
	print('  '*(number_rows-row-1)+'* '*(row+1))
for row in range(number_rows-1):
	print('  '*(row+1)+'* '*(number_rows-row-1))

''' 
Here the number of spaces and symbol 
are taken into account and a shortcut formula
is made to print the pattern.

12345  => let say number_rows=5
------
####* |1 In this the'#'symbol represents the spaces
###** |2 and is rest is part of pattern.
##*** |3  In the first half of the pattern i.e 
#**** |4  till the ---  
***** |5  Number of spaces for row 1 is 4(####) a
-------   and for row 2 is 3(###), for row 3 is 
#**** |1  2(##) and so on this leads to as similarity 
##*** |2  that is [number of rows(number_rows)-rownumber(row)-1]
###** |3  and star symbol can be printed by [rownumber(row)+1] 
####* |4  for second part of the pattern (after ---), 
-------   the number of spaces becomes 1(#) for row 1 and
 
2(##) for row 2 and 3(##) for row 3 and so on, also notice 
the number of rows for the bottom part of the pattern is number of rows
originally given minus 1 (rows_bottom_part=number_rows-1), hence
the formula for printing spaces is [rownumber(row)+1 if rownumber starts at 0]
and for printing stars the formula is [number of rows(number_rows)-rownumber(row)-1] 

Also note that while printing space in the pattern, the space aswell as the separation space
is taken care of i.e. ('  ') in the program is (<sapce><space>)
and for space near star is('*'<space>)
'''
