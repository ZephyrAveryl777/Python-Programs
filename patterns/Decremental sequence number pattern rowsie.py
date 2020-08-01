'''
Pattern 
Decremental sequence number pattern rowise
Enter number of rows: 5
Enter number of columns: 5
55555
54444
54333
54322
54321
'''
#origianl
print('Decremental sequence number pattern rowsie: ')
number_rows = int(input('Enter number of rows: '))
number_columns= int(input('ENter number of columns: '))
for row in range(number_rows,0,-1):
    for column in range(number_columns,0,-1):
        if column >=row :
            print(column, end=' ')
        else:
            print(row, end=' ')
    print()

