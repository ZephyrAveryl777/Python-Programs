'''
Problem Description:
--------------------
The program reads a file and counts 
the number of blank spaces in a text file.
'''
print(__doc__)
print('-'*25)
fileName=input('Enter file name: ')
k=0
with open(fileName,'r')as f:
	for line in f:
		words=line.split()
		for i in words:
			for letter in i:
				if letter.isspace:
					k+=1
print('Occurance of blank space in text file \'{%s}\' is %d times'%(fileName,k))