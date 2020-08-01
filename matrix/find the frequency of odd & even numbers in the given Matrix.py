print('''
Program to find the frequency of odd and even numbers in the given Matrix.
'''
)
matrix=[]
row=int(input('Enter size of row of the matrix: '))
column=int(input('Enter size of column of the matrix: '))
for i in range(row):
	a=[]
	for j in range(column):
		j=int(input('Enter elements of the matrix: '))
		a.append(j)
	print()
	matrix.append(a)
print('elements of the matrix: ')
for i in range(row):
	for j in range(column):
		print(matrix[i][j],end=" ")
	print()
countOdd=0
countEven=0
#count the numbers of even elements of the matrix: 
for i in range(row):
	#a=[]
	for j in range(column):
		if matrix[i][j]%2==0:
			#j=matrix[i][j]%2==o
		    #a.append(j)
			countEven=countEven+1
		else:
			#a.append(j)
			countOdd=countOdd+1
print('Frequency of odd numbers in matrix {}'.format(countOdd))
print(f'Frequency of even numbers in the matrix: {countEven}')