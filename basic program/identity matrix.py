print("-------Identity Matrix-----------")
n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()
    
print("----------Equivalent Matrix------------")
n=int(input("Enter a number : "))
for i in range(0,n):
    for j in range(0,n):
        print(n,sep=" ",end=" ")
    print()
    
print("---------Matrix-------------")
R = int(input("Enter the number of rows: ")) 
C = int(input("Enter the number of columns: ")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()


