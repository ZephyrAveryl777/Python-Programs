# a Python program to test Collatz conjecture for a given number

"""The Collatz conjecture is a conjecture that a particular sequence always reaches 1. 
The sequence is defined as
start with a number n. 
The next number in the sequence is n/2 if n is even and 3n + 1 if n is odd.

Problem Solution
1. Create a function collatz that takes an integer n as argument.
2. Create a loop that runs as long as n is greater than 1.
3. In each iteration of the loop, update the value of n.
4. If n is even, set n to n/2 and if n is odd, set it to 3n + 1.
5. Print the value of n in each iteration.
"""
def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    print(1, end='')
 
 
n = int(input('Enter n: '))
print('Sequence: ', end='')
collatz(n)