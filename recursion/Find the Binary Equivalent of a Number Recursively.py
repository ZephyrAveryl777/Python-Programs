'''
Problem Description:
-------------------
The program takes a 
number and finds the 
binary equivalent of 
a number recursively.
'''
print(__doc__,end="")
print('-'*20)
l=[]
def convert(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    convert(b//2)
a=int(input("Enter a number: "))
convert(a)
l.reverse()
print("Binary equivalent: ",end="")
for i in l:
    print(i,end=""),