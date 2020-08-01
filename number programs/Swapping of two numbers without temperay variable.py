##Problem Description
##The program takes both the values from the user and swaps them 
print("-------------------------------Method 1-----------------------")
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("Before swapping  First Number is {0} and Second Number is {1}" .format(a,b))
a=a+b
b=a-b
a=a-b
print("After swapping First number is {0} and Second Number is {1}".format(a,b))
print("-------------------------------Method 2-----------------------")
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("Before swapping  First Number is {0} and Second Number is {1}" .format(a,b))
a=a*b
b=a//b
a=a//b
print("After swapping First number is {0} and Second Number is {1}".format(a,b))
print("-------------------------------Method 3-----------------------")
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("Before swapping  First Number is {0} and Second Number is {1}" .format(a,b))
temp= a
a=b
b=temp
print("After swapping  First Number is {0} and Second Number is {1}" .format(a,b))
print("-------------------------------Method 4-----------------------")
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("Before swapping  First Number is {0} and Second Number is {1}" .format(a,b))
a = a ^ b
b= a ^ b
a = a ^ b
print("After swapping  First Number is {0} and Second Number is {1}" .format(a,b))
