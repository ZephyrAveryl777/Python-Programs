'''
Pattern 
Hollow Diamond Star Pattern
Enter number of stars: 5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''
number_rows= int(input('Enter number of rows: '))
for row in range(0,number_rows):
  for column in range(0,number_rows):
      if row+column==((number_rows-1)//2) or column-row==((number_rows-1)//2) or row-column==((number_rows-1)//2) or row+column==((((number_rows-1)//2)*2)+((number_rows-1)//2)):
        print('*',end='')
      else:
        print(' ',end='')
  print('\n',end='')

# print(((((number_rows-1)//2)*2)+((number_rows-1)//2)))
