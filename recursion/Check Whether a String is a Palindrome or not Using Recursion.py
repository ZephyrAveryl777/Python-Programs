'''
Problem Description:
-------------------
The program takes a 
string and checks whether a 
string is a palindrome or not 
using recursion.
'''
print(__doc__,end="")
print('-'*25)
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string: "))
if(is_palindrome(a)==True):
    print(f"String \'{a}\', is a palindrome!")
else:
    print(f"String \'{a}\', isn't a palindrome!")