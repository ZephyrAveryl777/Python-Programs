'''
Problem Description:
-------------------
The program reads a file and capitalizes 
the first letter of every word in the file.
'''
print(__doc__,end="")
print('-'*25)
fileName=input('Enter file name: ')
print('-'*35)
print(f'Contents of the file are : ')
with open(fileName,'r') as f:
	for line in f:
		l=line.title()
		print(l)