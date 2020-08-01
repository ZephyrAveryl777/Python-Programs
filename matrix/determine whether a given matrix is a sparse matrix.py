print("""
Note!
A matrix is said to be sparse matrix if most of the elements of that matrix are 0.
It implies that it contains very less non-zero elements.
""")
# To check whether the given matrix is the sparse matrix or not, 
# we first count the number of zero elements present in the matrix. 
# Then calculate the size of the matrix. 
# For the matrix to be sparse, count of zero elements present in an array must be greater than size/2.
matrix=[]
row=int(input("Enter row size of the matrix: "))
column=int(input("Enter column size of the matrix: "))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input(f"Enter elements of the matrix at poistion row({i})column({j}): "))
		a.append(j)
	print()
	matrix.append(a)
print("Elements of the matrix: ")
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print()
count =0
#Calculate the size of the array
size=row*column
#count all zero elements present in matrix
for i in range(row):
	for j in range(column):
		if matrix[i][j]==0:
			count=count+1

if count>size/2:
	print("Given matrix is a sparse matrix")
else:
	print("Given matrix is not a sparse matrix")

