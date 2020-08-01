"""
Example:
Enter number: 5
E D C B A
 D C B A
  C B A
   B A
    A
"""
print('Alphabet pattern: ')
number_rows= int(input("Enter number: "))
for row in range(1,number_rows+1):
    print(" "*(row-1),end="")
    for column in range(1,number_rows+2-row):
        print(chr(65+number_rows+1-row-column),end=" ")
    print()