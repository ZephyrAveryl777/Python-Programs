'''
Pattern 
Enter number of rows: 5
    5
   44
  333
 2222
11111
'''
print('Pattern')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,number_rows-row+1):
		print('  ',end=' ')
	for column in range(1,row+1):
		if (number_rows-row+1) < 10:
			print(f'0{number_rows-row+1}',end=' ')
		else:
			print(number_rows-row+1,end=' ')
	print()