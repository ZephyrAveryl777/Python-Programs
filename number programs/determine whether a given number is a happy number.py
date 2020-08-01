"""
Happy number:
The happy number can be defined as
a number which will yield 1 when it is replaced by the sum of the square of its digits repeatedly. 
If this process results in an endless cycle of numbers containing 4,then the number is called an unhappy number.
For example, 32 is a happy number as the process yields 1 as follows
3**2 + 2**2 = 13
1**2 + 3**2 = 10
1**2 + 0**2 = 1
Some of the other examples of happy numbers are 7, 28, 100, 320 and so on.
The unhappy number will result in a cycle of 4, 16, 37, 58, 89, 145, 42, 20, 4, ....
To find whether a given number is happy or not, 
calculate the square of each digit present in number and add it to a variable sum. 
If resulting sum is equal to 1 then, given number is a happy number. 
If the sum is equal to 4 then, the number is an unhappy number. 
Else, replace the number with the sum of the square of digits.
"""
#isHappyNumber() will determine whether a number is happy or not  
num=int(input("Enter a number: "))
def isHappyNumber(num):  
    rem = sum = 0  
      
    #Calculates the sum of squares of digits  
    while(num > 0):  
        rem = num%10  
        sum = sum + (rem*rem)  
        num = num//10  
    return sum       
result = num  
while(result != 1 and result != 4):  
    result = isHappyNumber(result)  
   
#Happy number always ends with 1  
if(result == 1):  
    print(str(num) + " is a happy number")  
#Unhappy number ends in a cycle of repeating numbers which contain 4  
elif(result == 4):  
    print(str(num) + " is not a happy number")