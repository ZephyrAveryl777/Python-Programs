'''
Pattern:
Enter number of rows: 5
     A
    C B A
   E D C B A
  G F E D C B A
 I H G F E D C B A
'''
print('Alphabet pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	print(' '*(number_rows-row),end=' ')
	for column in range(65+2*row-2,64,-1):
		print(chr(column),end=' ')
	print()