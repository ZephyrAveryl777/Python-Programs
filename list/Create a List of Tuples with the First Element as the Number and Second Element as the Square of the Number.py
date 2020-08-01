"""
Problem Description
The program takes a range and creates a list of tuples within that range with
the first element as the number and the second element as the square of the number.
Problem Solution
1. Take the upper and lower range for the numbers from the user.
2. A list of tuples must be created using list comprehension where
the first element is the number within the range and the second element is the square of the number.
3. This list of tuples is then printed.
4. Exit.
"""
lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
a=[(x,x**2) for x in range(lower,upper+1)] # comprehension loop
print(a)