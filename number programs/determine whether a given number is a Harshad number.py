"""
Program to determine whether a given number is a Harshad number
Harshad number
A number is said to be the Harshad number if it is divisible by the sum of its digit.
For example, if number is 156, then sum of its digit will be 1 + 5 + 6 = 12. Since 156 is divisible by 12. 
So, 156 is a Harshad number.
Some of the other examples of Harshad number are 8, 54, 120, etc.
To find whether the given number is a Harshad number or not, calculate the sum of the digit of the number then, 
check whether the given number is divisible by the sum of its digit. 
If yes, then given number is a Harshad number."""
num = int(input("Enter a number: "));  
rem = sum = 0;  
   
#Make a copy of num and store it in variable n  
n = num;  
   
#Calculates sum of digits  
while(num > 0):  
    rem = num%10;  
    sum = sum + rem;  
    num = num//10;  
   
#Checks whether the number is divisible by the sum of digits  
if(n%sum == 0):  
    print(str(n) + " is a harshad number");  
else:  
    print(str(n) + " is not a harshad number");  