""""Problem Description
The program takes two numbers and prints the LCM of two numbers."""
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
	min=a
else:
	min=b
while 1:
	if min%a == 0 and min%b == 0:
		print(f"LCM of the numbers {a} and {b} is: {min}")
		break
	min=min+1