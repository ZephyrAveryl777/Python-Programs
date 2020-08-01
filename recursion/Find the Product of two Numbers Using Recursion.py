'''
Problem Description:
--------------------
The program takes 
two numbers and finds 
the product of two numbers 
using recursion.
'''
print(__doc__,end="")
print('-'*25)
def product(a,b):
    if(a<b):
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:
        return 0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Product %d and %d is: %d" %(a,b,product(a,b)))