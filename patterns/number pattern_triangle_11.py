'''
Pattern
Enter number of rows: 5
    2
   242
  24642
 2468642
2468108642
'''
print('Number pattern: ')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows+1):
	for column in range(row,number_rows):
		print('  ',end=' ')
	for column in range(2,(row*2)+1,2):
		if column < 10:
			print(f' {column}',end=' ')
		else:
			print(column,end=' ')
	for column in range((row-1)*2,1,-2):
		if  column < 10:
			print(f' {column}',end=' ')
		else: 
			print(column,end=' ')
	print()
