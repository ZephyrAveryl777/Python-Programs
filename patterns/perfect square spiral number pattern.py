print("perfect square spiral number pattern: ")
def pattern(N, a=1,b=0):
    if N>0:
        lst[b]=N
        if a<=2:
            if a==1: pattern(N-1,2,b+1)
            else: pattern(N,a-1,b+1)
            
def fill(subcount, N=1, row=0, col=0, direction=0, count=0):
    arr[row][col]=N
    if N<Number*Number:
        if subcount==1:
            direction=direction+1
            count=count+1
            subcount=lst[count]
        else: subcount=subcount-1  
        if direction%4==0:
            col=col+1
        elif direction%4==1:
            row=row+1
        elif direction%4==2:
            col=col-1
        else: row=row-1
        
        fill(subcount,N+1,row,col,direction,count)

def Disp(N,a=0):
    if N<Number:
    	#With Spaces as per the biggest numbers which are in the middle row
        print(arr[N][a], end=' '*(1+len(str(arr[Number//2][a]))-len(str(arr[N][a])) ) )
        if a<Number-1:
            Disp(N,a+1)
        else:
            print('')
            Disp(N+1,0)
           
Number = int(input('Enter number of rows: '))
#Create zeroes Matrix
arr = [x[:] for x in [[0] * Number] * Number]  
lst = [None] * (Number*2-1)
pattern(Number)
fill(lst[0])
Disp(0)
