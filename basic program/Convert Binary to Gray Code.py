"""
Problem Description
We are given a binary number. We have to find the associated Gray codeword.
Problem Solution
1. The function binary_to_gray is defined.
2. It takes the binary number as a string as argument.
3. It returns its associated Gray codeword as a string.
4. If b(i) is the ith bit in the binary number and g(i) is the ith bit in its associated Gray codeword
 where the 0th bit is the MSB, 
it can be shown g(0) = b(0) and g(i) = b(i) XOR b(i – 1) for i > 0.
5. Thus a binary number b can be converted to its associated Gray codeword by performing b XOR (b >> 1).
"""
def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2) # convert to int
    n ^= (n >> 1)
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]
 
 
g = input('Enter binary number: ')
b = binary_to_gray(g)
print(f"Gray codeword: {b}")

