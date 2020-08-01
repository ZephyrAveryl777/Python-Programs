import math
print(f"---------------------METHOD 1 using math.gcd()---------------------")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(f"The GCD of the two numbers {a} and {b} is: {math.gcd(a,b)}")

print(f"\n-----------------------METHOD 2 using Recursions-------------------")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def hcf(a,b):
	if b==0:
		return a 
	else:
		return hcf(b, a%b)
print(f"The GCD of the two numbers {a} and {b} is: {hcf(a,b)}")

print(f"\n--------------------------METHOD 3 using loops---------------------")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def computeGCD(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i     
    return gcd 
print(f"The GCD of the two numbers {a} and {b} is : {computeGCD(a,b)}")

print(f"\n--------------------------METHOD 4 using Euclidean Algorithm---------------")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def computeGCD(x,y):
	while y:
		x,y = y,x%y
	return x
print(f"The GCD of The two numbers {a} and {b} is : {computeGCD(a,b)}")