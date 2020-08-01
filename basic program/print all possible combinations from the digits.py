##Problem Description
##The program takes three distinct numbers and prints all possible combinations from the digits.
while True:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=int(input("Enter the third number: "))
    d=[]
    d.append(a)
    d.append(b)
    d.append(c)
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if(i!=j and j!=k and k!=i):
                    print(d[i],d[j],d[k])
    print("-----------------------------")
    continue
