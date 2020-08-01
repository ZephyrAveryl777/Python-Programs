##Problem Description
##The program takes the upper and lower limit and prints all odd numbers within a given range.
while True: 
    lower=int(input("Enter the lower limit of the range: "))
    upper =int(input("Enter the upper limit of the range: "))
    d=[]
    for i in range(lower,upper+1):
        if(i%2!=0):
            d.append(i)
    print("odd numbers in the range are: ",d)
    print("-------------------------------------------------")
    continue
## for even numbers the if conditon becomes i!2==0
