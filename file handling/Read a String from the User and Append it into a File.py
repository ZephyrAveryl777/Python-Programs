'''
Problem Description:
-------------------
The program takes a string from the user 
and appends the string into an existing file.
'''
print(__doc__)
print('-'*25)
fileName=input('Enter file name along with path: ')
file3=open(fileName,"a")
string=input('Enter string to append: ')
file3.write(string)
file3.close()
print('Contents of appended file: ')
print('-'*25)
file4=open(fileName,"r")
line1=file4.readline()
while line1!="":
	print(line1)
	line1=file4.readline()
file4.close()