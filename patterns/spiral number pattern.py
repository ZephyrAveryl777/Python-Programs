'''
Pattern:
Spiral number pattern:
Enter number of rows: 5
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
'''
n=int(input('Enter number of rows: '))
for row in range(0,2*n-1):
	for column in range(0,(2*n-1)):
		min= row if row < column else column
		min= min if min < ((n*2)-1)-row-1 else (((n*2)-1)-row)-1
		min= min if min < (((n*2)-1)-column) else (((n*2)-1)-column)-1
		print(n-min,end=' ')
	print()