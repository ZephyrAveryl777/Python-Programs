"""
Pattern
Enter number: 5
    A
   B B
  C C C
 D D D D
E E E E E
 D D D D
  C C C
   B B
    A
"""
print('Alphabet pattern:')
number_rows = int(input("Enter number of rows: "))
for row in range(1,number_rows+1):
    print(" "*(number_rows-row),end="")
    for column in range(1,row+1):
        print(chr(64+row),end=" ")
    print()
for row in range(1,number_rows):
    print(" "*row,end="")
    for column in range(1,number_rows+1-row):
        print(chr(64+number_rows-row),end=" ")
    print()