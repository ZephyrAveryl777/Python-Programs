'''
Problem Description
The program takes a letter from the user 
and counts the number of occurrences of 
that letter in a file.
'''
fileName=input('Enter the  file Name: ')
character=input('Enter letter to be searched: ')
k=0
with open(fileName,'r') as f:
	for line in f:
		words=line.split()
		for i in words:
			for letter in i:
				if letter==character:
					k+=1
print(f'Occurance of letters \'{character}\' is: {k}')