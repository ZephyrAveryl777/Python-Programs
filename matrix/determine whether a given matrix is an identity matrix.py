#identity matrix
matrix=[]
row=int(input("Enter row size of matrix: "))
column=int(input("Enter column size of matrix: "))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input(f"Enter element in row({i})column({j}): "))
		a.append(j)
	print()
	matrix.append(a)
print("elements of the matirx are: ")
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print(" ")


flag=True
if row!=column:
	print("matrix should be a square matrix.")
else:
	#Check if diagonal elements are equal to 1 and rest of elements are 0
	for i in range(row):
		for j in range(column):
			if i==j and matrix[i][j]!=1:
				flag=False
				break
			if i!=j and matrix[i][j]!=0:
				flag=False
				break
	if(flag):
		print("Given matrix  is an identity matrix.")
	else:
		print("Given matrix  is not an identity matrix.")
