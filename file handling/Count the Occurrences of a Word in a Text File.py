'''
Problem Description:
--------------------
The program takes a word from the user 
and counts the number of occurrences of 
that word in a file.
'''
print(__doc__)
print('-'*25)
fname = input("Enter file name: ")
word=input("Enter word to be searched: ")
k = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                k=k+1
print("Occurrences of the word \'%s\' is: %s"%(word,k))