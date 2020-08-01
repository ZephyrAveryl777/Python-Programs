print("-------------METHOD 1 using Sieve of Eratosthenes--------------------")
n=int(input("Enter upper limit of range: "))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,end="\t")
    sieve-=set(range(prime,n+1,prime))
    print()
   

print("--------------METHOD 2 using loop------------------------------------")
r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)
