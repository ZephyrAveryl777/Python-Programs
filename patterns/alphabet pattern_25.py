"""
Pattern:
Enter a number: 5
     A
    B B
   C C C
  D D D D
 E E E E E
"""
print('Alphabet Pattern:')
number_rows = int(input("Enter a number: "))
for row in range(1, number_rows+1):
    print(" "*(number_rows-row),end=" ")
    for column in range(1,row+1):
        print(chr(64+row),end=" ")
    print()
