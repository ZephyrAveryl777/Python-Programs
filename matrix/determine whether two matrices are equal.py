print('''
Note!
Two matrices are said to be equal if and only if they satisfy the following conditions:
*> Both the matrices should have the same number of rows and columns.
*> Both the matrices should have the same corresponding elements.
''')
first_matrix=[]
first_row=int(input('Enter size of row of first matrix: '))
first_column=int(input('Enter size of column of first matrix: '))
for i in range(first_row):
	a=[]
	for j in range(first_column):
		j=int(input(f'Enter elements of matrix at position row({i})column({j}): '))
		a.append(j)
	print()
	first_matrix.append(a)
print('elements of the first matrix: ')
for i in range(first_row):
	for j in range(first_column):
		print(first_matrix[i][j],end=" ")
	print()
second_matrix=[]
second_row=int(input('Enter size of row of second matrix: '))
second_column=int(input('Enter size of column of second matrix: '))
for i in range(second_row):
	a=[]
	for j in range(second_column):
		j=int(input(f'Enter elements of matrix at position row({i})column({j}): '))
		a.append(j)
	print()
	second_matrix.append(a)
print('elements of the second matrix: ')
for i in range(second_row):
	for j in range(second_column):
		print(second_matrix[i][j],end=" ")
	print()
flag=True
#checks if dimensions of both matrices are equal
if first_row != second_row or first_column != second_column:
	print('Matrices are not equal')
else:
	for i in range(first_row):
		for j in range(first_column):
			if first_matrix[i][j]!=second_matrix[i][j]:
				flag=False
				break
if(flag):
	print('Matrices are equal')
else:
	print('Matrices are not equal')