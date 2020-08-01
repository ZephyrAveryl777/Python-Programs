'''
Pattern
Enter number of rows: 5
22464
2246
224
22
2
'''
import math 
print('number pattern: ')
number=int(input('Enter number: '))
while math.floor(math.log10(number)+1)!=0:
        print('%d\n'%number,end='')
        number/=10
print()
