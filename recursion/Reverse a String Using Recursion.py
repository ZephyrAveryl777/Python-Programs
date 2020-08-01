'''
Problem Description:
--------------------
The program takes a string and reverses 
the string using recursion.
'''
print(__doc__,end="")
print('-'*30)
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(f'Reversal of string \'{a}\' is: {reverse(a)}')