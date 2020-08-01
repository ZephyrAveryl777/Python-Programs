print('''
Note!
Transpose of a matrix can be found by interchanging rows with the column that is, 
rows of the original matrix will become columns of the new matrix. 
Similarly, columns in the original matrix will become rows in the new matrix. 
If the dimension of the original matrix is 2 × 3 then, 
the dimensions of the new transposed matrix will be 3 × 2.
''')
matrix=[]
row=int(input('enter size of row of matrix: '))
column=int(input('enter size of column of matrix: '))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input(f'enter elements of matrix at poistion row({i})column({j}): '))
		a.append(j)
	print()
	matrix.append(a)
print('Elements of matrix: ')
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print()

#Declare array t with reverse dimensions and is initialized with zeroes.  
t = [[0]*row for i in range(column)]; 

#calcutaes transpose of given matrix
for i in range(column):
	for j in range(row):
		#converts the row of original matrix into column of transposed matrix
		t[i][j]=matrix[j][i]
print('transpose of given matrix: ')
for i in range(column):
	for j in range(row):
		print(t[i][j],end=" ")
	print()