"""
Pattern
Enter a number_rowsber: 5
     E
    D E
   C D E
  B C D E
 A B C D E
  B C D E
   C D E
    D E
     E
"""
print('Alphabet Pattern: ')
number_rows = int(input("Enter a number_rowsber: "))
for row in range(1,number_rows+1):
    print(" "*(number_rows-row),end=" ")
    for column in range(0,row):
        print(chr(65+number_rows+column-row),end=" ")
    print()
for column in range(1,number_rows):
    print(" "*column,end=" ")
    for column in range(0,number_rows-column):
        print(chr(65+column+column),end=" ")
    print()