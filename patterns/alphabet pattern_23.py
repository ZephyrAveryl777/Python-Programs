'''
Pattern: 
Enter a number: 5
E 
E D 
E D C 
E D C B 
E D C B A 
E D C B 
E D C 
E D 
E 
'''
print('Alphabet Pattern: ')
number_rows = int(input("Enter a number: "))
for row in range(1,number_rows+1):
    for column in range(1,row+1):
        print(chr(65+number_rows-column),end=" ")
    print()
for row in range(1,number_rows+1):
    for column in range(number_rows-row,0,-1):
        print(chr(64+column+row),end=" ")
    print()