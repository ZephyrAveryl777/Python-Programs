'''
Pattern 
Enter number of rows: 5
        1
      123
    12345
  1234567
123456789
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(1,((number_rows-row)*2)+1):
		print(' ',end=' ')
	for column in range(1,(2*row)):
		print(column,end=' ')
	print()
