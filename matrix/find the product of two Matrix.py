print('''
The product of two matrices can be computed
by multiplying elements of the first row of 
the first matrix with the first column of
the second matrix then, add all the product 
of elements. Continue this process until each 
row of the first matrix is multiplied with 
each column of the second matrix.
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
#For two matrices to be multiplied
#number of columns in the first matrix must be equal to the number of rows in the second matrix  
if first_column != second_row:
	print('matrices cannot be multiplied!')
else:
	#Array prod will hold the result and is initialized with zeroes.
	product=[[0 for j in range(0,second_column)]for i in range(0,first_row)]


#performs product of matrices a and b. Stores the result in matrix prod
for i in range(first_row):
	 for j in range(second_column):
	 	  for k in range(second_row):
	 	  	product[i][j]=product[i][j]+(first_matrix[i][k] * second_matrix[k][j])

print('product of two matrices:')
for i in range(first_row):
	for j in range(second_column):
		print(product[i][j],end=" ")
	print()	
