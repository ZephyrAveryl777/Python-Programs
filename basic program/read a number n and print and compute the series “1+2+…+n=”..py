##Problem Description
##The program takes a number n and prints and computes the series “1+2+…+n=”.
n=int(input("Enter a number: "))
a=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))
 
print()
