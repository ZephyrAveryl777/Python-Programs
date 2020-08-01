##Problem Description
##The program takes in an integer and prints the smallest divisor of the integer.
while 1:
    n=int(input("Enter a number: "))
    a=[]
    for i in range(2,n+1):
        if n%i==0:
            a.append(i)
    print("The divisors of the number {0} are {1}".format(n,a))
    a.sort()
    print("Smallest divisor is: ",a[0])
    print("------------------------------")
    continue
