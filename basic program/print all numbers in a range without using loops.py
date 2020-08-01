def printno(upper):
    if(upper>0):
        printno(upper-1)
        print(upper)
upper=int(input("Enter upper limit: "))
printno(upper)