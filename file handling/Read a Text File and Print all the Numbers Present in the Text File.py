'''
Problem Description:
-------------------
The program takes the name of a file 
from the user and prints all the numbers 
present in the text file.
'''
print(__doc__)
print('-'*25)
fname = input("Enter file name: ")
l=[]
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    l.append(letter)
print(f'All the numbers in the file are: {l}')