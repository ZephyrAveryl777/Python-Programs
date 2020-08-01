'''
Pattern 9
Mirrored right triangle star 
Enter number of rows: 5
    *
   **
  ***
 ****
*****
'''
print('Mirrored right triangle star pattern:')
rows=int(input('Enter number of rows:'))
for i in range(0,rows):
	for j in range(0,rows-i):
		print('*',end=' ')
	print('\n', end="")