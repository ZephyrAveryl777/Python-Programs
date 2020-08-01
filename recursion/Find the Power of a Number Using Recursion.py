'''
Problem Description:
--------------------
The program takes a base and a 
power and finds the power of 
the base using recursion.
'''
print(__doc__,end="")
print('-'*25)
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print(f"Result of {base} to the power of {exp} is {power(base,exp):,d} : ")