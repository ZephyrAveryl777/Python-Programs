'''
Problem Description:
------------------
The program takes a file name from the user and 
reads the contents of the file in reverse order.
'''
print(__doc__,end="")
print('-'*25)
fileName=input('Enter file name: ')
print('-'*40)
print('Contents of text in reversed order are: ')
for line in reversed(list(open(fileName))):
	print(line.rstrip())