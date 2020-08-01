'''
Problem Description
-------------------
The program takes two numbers and 
finds the LCM of two numbers using recursion.
'''
print(__doc__,end="")
print('-'*20)
def lcm(a,b):
    lcm.multiple=lcm.multiple+b
    if((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple;
    else:
        lcm(a, b)
    return lcm.multiple
lcm.multiple=0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if(a>b):
    LCM=lcm(b,a)
else:
    LCM=lcm(a,b)
print(f'LCM of {a} and {b} is : {LCM}')