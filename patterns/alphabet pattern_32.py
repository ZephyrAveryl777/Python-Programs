"""
Pattern:
    Enter the number of input: 5
    E D C B A
    E D C B A
    E D C B A
    E D C B A
    E D C B A

"""
print('Alphabet Pattern: ')
number_rows = int(input("Enter the number of rows: "))
for row in range(1, number_rows + 1):
    for column in range(1, number_rows + 1):
        print(chr(65+number_rows-column), end=" ")
    print()
