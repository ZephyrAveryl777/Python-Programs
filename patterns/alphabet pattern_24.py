"""
Pattern:
Enter a number: 5
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
print('Alphabet Pattern:')
number_rows = int(input("Enter a number: "))
for row in range(1, number_rows+1):
    for column in range(1,row+1):
        print(chr(64+number_rows-row+column),end=" ")
    print()
for row in range(1,number_rows+1):
    for column in range(1, number_rows-row+1):
        print(chr(64+column+row),end=" ")
    print()
