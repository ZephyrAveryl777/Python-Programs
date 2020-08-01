##n=int(input("Enter upper limit of range: "))
##sieve=set(range(2,n+1))
##while sieve:
##    prime=min(sieve)
##    print(prime,end="\t")
##    sieve-=set(range(prime,n+1,prime))
## 
##print()

N=int(input("Input the value of N: "))
Primes=[True for k in range(N+1)]
p=2
Primes[1]=False
Primes[0]=False
while(p*p<=N):
    if Primes[p]==True:
        for j in range(p*p,N+1,p):
            Primes[j]=False
    p+=1
for i in range(2,N):
    if Primes[i]:
        print(i,end=' ')          
