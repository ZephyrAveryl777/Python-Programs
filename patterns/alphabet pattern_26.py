"""
Pattern:
Enter a number: 5
     A
    A B
   A B C
  A B C D
 A B C D E
"""
print('Alphabet Pattern: ')
number_rows = int(input("Enter number of rows: "))
for row in range(1, number_rows+1):
    print(" "*(number_rows-row),end=" ")
    for column in range(1,row+1):
        print(chr(64+column),end=" ")
    print()