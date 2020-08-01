matrix=[]
row=int(input('Enter size of row: '))
column=int(input('enter size of column: '))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input(f'enter elements of the matrix at postion row({i})column({j}): '))
		a.append(j)
	print()
	matrix.append(a)
print('Elements of matrix: ')
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print()
#calculates sum of each row of given matrix
for i in range(row):
	sumRow=0
	for j in range(column):
		sumRow=sumRow+matrix[i][j]
	print(f'sum of row {i+1} is: {sumRow}')
#calculates sum of each column of given matrix
for i in range(row):
	sumColumn=0
	for j in range(column):
		sumColumn=sumColumn+matrix[j][i]
	print(f'sum of column {i+1} is: {sumColumn}')

