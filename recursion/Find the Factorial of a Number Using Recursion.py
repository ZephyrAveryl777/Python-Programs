'''
Problem Description
--------------------
The program takes a number and determines the factorial 
of the number using recursion.
'''
print(__doc__)
print('-'*15)
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number: "))
print(f"Factorial of {n} is: {factorial(n)}")