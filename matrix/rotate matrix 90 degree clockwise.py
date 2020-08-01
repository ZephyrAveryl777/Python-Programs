print('''
To rotate matrix elements clockwise.
the idea is to in-place conver the matrix into its transpose 
then swap first column with the last column, 
second column with the second last column, and so on...
''')
matrix=[]
row=int(input('Enter size of row: '))
column=int(input('Enter size of column: '))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input(f'Enter elements of matrix at positon row({i})column({j}): '))
		a.append(j)
	print()
	matrix.append(a)
print('elements of the matrix: ')
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print()
# to rotate a matrix
# if row != column:
# 	print('matrix is not square matrix hence rotation is difficult')
# else: 
# 	N=row=column
temp = [[0]*row for i in range(column)]
#Transpose the amtrix
for i in range(row):
	for j in range(column):
		temp[i][j]=matrix[j][i]
#swap columns
for i in range(row):
	for j in range(column):
		temp[i][j]=matrix[row-j-1][i]

#rotate_matrix=[[0 for j in column] for i in range(row) ]
print('after rotating the matrix: ')
for i in range(row):
	for j in range(column):
		print(temp[i][j],end=" ")
	print()
