'''
Problem Description
------------------- 
The program takes the number 
of terms and determines the 
fibonacci series using recursion 
upto that term.
'''
print(__doc__)
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
print('-'*25)
n = int(input("Enter number of terms: "))
print("Fibonacci sequence: ",end="")
a=[]
for i in range(n):
	a.append(fibonacci(i))
print(a)