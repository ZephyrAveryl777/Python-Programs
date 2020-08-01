"""
Example:
Enter number: 5
A B C D E
 A B C D
  A B C
   A B
    A
"""
print('Alphabet Pattern: ')
number_rows = int(input("Enter number of rows: "))
for row in range(1,number_rows+1):
    print(" "*(row-1),end="")
    for column in range(1,number_rows+2-row):
        print(chr(64+column),end=" ")
    print()