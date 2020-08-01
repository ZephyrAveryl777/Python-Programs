'''
Problem Description
-------------------
The program takes two numbers 
and finds the GCD of two numbers 
using recursion.
'''
print(__doc__,end="")
print('-'*20)
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
GCD=gcd(a,b)
print(f"GCD of {a} and {b} is: {GCD}")
