'''
Pattern:
Enter number of rows: 5
        1
      123
    12345
  1234567
123456789
  1234567
    12345
      123
        1      
'''
print('Number Pattern: ')
number_rows=int(input('Enter number of rows:'))
for row in range(1,number_rows+1):
	for column in range(row*2,number_rows*2):
		print(' ',end=' ')
	for column in range(1,(2*row-1)+1):
		print(column,end=' ')
	print()
for row in range(number_rows-1,0,-1):
	for column in range(row*2,number_rows*2):
		print(' ',end=' ')
	for column in range(1,(2*row-1)+1):
		print(column,end=' ')
	print()
