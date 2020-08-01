temp=n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
    print(f"natural numbers in series {sum1}+{n}")  
print(f"The sum of first {temp} natural numbers is: {sum1}")