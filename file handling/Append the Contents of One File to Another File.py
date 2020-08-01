'''
Problem Description:
-------------------
The program takes the name of the file to be read 
from and the file to append into from the user 
and appends the contents of one file to another.
'''
print(__doc__)
print('-'*25)
fileName1=input('Enter file to read from: ')
fileName2=input('Enter file to be appended to: ')
fileInput=open(fileName1,"r")
data=fileInput.read()
fileInput.close()
fileOutput=open(fileName2,'a')
fileOutput.write(data)
fileOutput.close()