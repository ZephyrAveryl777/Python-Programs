'''
Pattern 
Heart star pattern:
Enter number of stars: 5
  *****     *****
 *******   *******
********* *********
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
'''
number_rows=int(input('Enter number of rows: '))
n=number_rows//2
for row in range(n):
	for column in range(n-row-1):
		print(' ',end='')
	for column in range(row+2):
		print('* ',end="")
	for column in range(2*(n-row-1)):
		print(' ',end='')
	for column in range(row+2):
		print('* ',end="")
	print()

for row in range(number_rows+2,0,-1):
	for column in range((number_rows+2)-row):
		print(' ',end='')
	for column in range(row,0,-1):
		print('* ',end='')
	print()