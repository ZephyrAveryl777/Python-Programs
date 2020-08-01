#Matrix subtraction
print("""
Note! 
Two matrices may be added or subtracted only
if they have the same dimension; that is, 
they must have the same number of rows and columns.
\n""")
matrix_a=[]
row=int(input("Enter size of row of first matrix: "))
column=int(input("Enter size of column of first matrix: "))
for i in range(row):
	a=[]
	for j in range(column):
		j = int(input(f"Enter element in row({i})column({j}): "))
		a.append(j)
	print()
	matrix_a.append(a)
print("elements of the matrix are: ")
for i in range(row):
	for j in range(column):
		print(matrix_a[i][j],end=" ")
	print(" ")
print()
matrix_b=[]
row=int(input("Enter size of row of second matrix: "))
column=int(input("Enter size of column of second matrix: "))
for i in range(row):
	a=[]
	for j in range(column):
		j = int(input(f"Enter element in row({i})column({j}): "))
		a.append(j)
	print()
	matrix_b.append(a)
print("elements of the matrix are: ")
for i in range(row):
	for j in range(column):
		print(matrix_b[i][j],end=" ")
	print(" ")
#array sum will hold the result and is initallised with zeroes
result=sum=[[0 for j in range(0,column)]for i in range(0,row)]
#Perform addition of matrices a and b. Store the  result in matrix sum
for i in range(row):
	a=[]
	for j in range(column):
		sum[i][j]=(matrix_a[i][j] - matrix_b[i][j])
		a.append(sum[i][j])
	print()
	result.append(a)
print("Subtraction of two matices : ")
for i in range(row):
    for j in range(column):
        print(result[i][j],end=" ")
    print()
