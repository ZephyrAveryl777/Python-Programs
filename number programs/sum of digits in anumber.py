##Problem Description
##The program takes in a number and finds the sum of digits in a number.
print("-------------------Method 1----------------------------------")
temp=n=int(input("Enter a number: "))
total = 0
while n>0 :
    total = total+(n%10)
    n=n//10
print("The total sum of digits in the number {0} is: {1} ".format(temp,total))
print("--------------------------------------------------------------")

print("-------------------Method 2----------------------------------")
l=[]
def sum_digits(b):
    if(b==0):
        return l
    l.append(b%10)
    sum_digits(b//10)
temp=n=int(input("Enter a number: "))
sum_digits(n)
print("The total sum of digits in the number {0} is: {1} ".format(temp,sum(l)))
print("--------------------------------------------------------------")

