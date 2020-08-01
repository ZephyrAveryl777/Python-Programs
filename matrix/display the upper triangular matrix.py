print('''
Lower triangular matrix is a square matrix in which all the elements above the principle diagonal will be zero. To find the lower triangular matrix, a matrix needs to be a square matrix that is, 
number of rows and columns in the matrix needs to be equal.
Dimensions of a typical square matrix can be represented by n x n.
''')
matrix=[]
row=int(input('Enter row sizeof matrix: '))
column=int(input('Enter column size of matrix: '))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input(f'Enter elements of matrix at position row({i})column({j}): '))
		a.append(j)
	print()
	matrix.append(a)
print('elements of the matrix: ')
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print()
if row!=column:
	print('Matrix should be of square matrix')
else:
    #Performs required operation to convert given matrix into lower triangular matrix  
    print('Lower triangular matrix: ')
    for i in range(0,row):
    	for j in range(0,column):
    		if j < i:
    			print('0')
    		else:
    			print(matrix[i][j],end=" ")
    	print(" ")
	
