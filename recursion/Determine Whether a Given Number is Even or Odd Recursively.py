'''
Problem Description
The program takes a number and determines 
whether a given number is even or odd recursively.

Problem Solution
1. Take a number from the user and store it in a variable.
2. Pass the number as an argument to a recursive function.
3. Define the base condition as the number to be lesser than 2.
4. Otherwise call the function recursively with the number minus 2.
5. Then return the result and check if the number is even or odd.
6. Print the final result.
7. Exit.
'''
def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print(f"Number {n} is even!")
else:
      print(f"Number {n} is odd!")