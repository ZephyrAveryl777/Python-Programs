'''
Problem Description
-------------------
The program takes a number 
and finds if the number is 
prime or not using recursion.
'''
print(__doc__,end="")
print('-'*25)
def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print(f"Number: {n}, is not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print(f"Number: {n}, is a prime")
        return 'True'
n=int(input("Enter number: "))
check(n) 