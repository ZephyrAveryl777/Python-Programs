##Problem Description
##The program takes a number and checks whether it is a palindrome or not.
print("--------------Method 1-----------------")
temp=n=int(input("Enter a number:"))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if(temp==rev):
    print("The number {} is a palindrome!".format(temp))
else:
    print("The number {} isn't a palindrome".format(temp))
print("---------------------------------")
 
print("--------------Method 2-----------------")
temp=n=int(input("Enter a number:"))
rev=0
def pali(n):
    global rev
    while n>0:
        rev=rev*10+(n%10)
        n=n//10
    return rev
rev=pali(n)
if(temp==rev):
    print("The number {} is a palindrome!".format(temp))
else:
    print("The number {} isn't a palindrome".format(temp))
print("---------------------------------")
