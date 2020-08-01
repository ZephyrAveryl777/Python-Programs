'''
Problem Description:
--------------------
The program takes the file name 
from the user and counts number 
of words in that file.
'''
print(__doc__)
print('-'*20)
fileName = input("Enter file name: ")
numberOfWords = 0
with open(fileName, 'r') as f:
    for line in f:
        words = line.split()
        numberOfWords += len(words)
print(f"Number of words in the file is: {numberOfWords}")