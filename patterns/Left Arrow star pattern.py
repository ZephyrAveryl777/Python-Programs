'''
Pattern
Right Arrow Pattern:
Enter number of rows: 5
*****
  ****
    ***
      **
        *
      **
    ***
  ****
*****
'''

# for printing upper part 
# of the arrow 
print('right arrow pattern:')
number_rows=int(input('Enter number of rows: '))
for row in range(1,number_rows): 
# To give space before printing 
# stars in upper part of arrow 
	for column in range(0,row): 
		print("  ",end="") 
	# To print stars in upper 
	# part of the arrow 
	for column in range(row,number_rows+1): 
		print("*",end="") 
	print() 
# for printing lower part 
# of the arrow 
for row in range(0,number_rows): 
# To give space before printing 
# stars in lower part of arrow 
	for column in range (row,number_rows): 
		print("  ",end="") 
	# To print stars in lower 
	# part of the arrow 
	for column in range (0,row+1): 
		print("*",end="") 
	print() 































# # Prints the upper part of the arrow 
# number_rows=int(input('Enter number of rows: '))
# for row in range(1, number_rows+1):  

# # for the spacing to form 
# # the point of the arrow 
# 	for column in range(row, number_rows):  
  
# 	    print(" ", end="") 
  
# # for printing the star(*) 
# 	for column in range(row, number_rows+1):  
  
# 	    print("*", end="") 
  
# 	print() 

# # Prints lower part of the arrow 
# for row in range(2, number_rows+1): 

# # for the spacing to form 
# # the point of the arrow 
# 	for column in range(1, row):  
  
# 	    print(" ", end="") 
  
# # for printing the star(*) 
# 	for column in range(1, row+1):  
  
# 	    print("*", end="") 
  
# 	print() 
