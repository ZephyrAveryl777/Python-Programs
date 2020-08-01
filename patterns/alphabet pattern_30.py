"""
Alphabet Pattern:
Example:
    Enter the number of input: 5
    E E E E E
    D D D D D
    C C C C C
    B B B B B
    A A A A A

"""
print('Alphabet Pattern:')
number_rows = int(input("Enter the number of input: "))
for row in range(1, number_rows + 1):
    for cloumn in range(1, number_rows + 1):
        print(chr(65+number_rows-row), end=" ")
    print()
