'''
Problem Description:
-------------------
The program takes the file name from the 
user and reads the contents of that file.
'''
print(__doc__,end="")
print('-'*25)
a=str(input('Enter the name of the file (dont forget the path) with .txt extension: '))
file2=open(a,'r')
line=file2.readline()
print(f'Text in the Text Document is: ')
print('-'*30)
while line!="":
	print(line)
	line=file2.readline()
file2.close()