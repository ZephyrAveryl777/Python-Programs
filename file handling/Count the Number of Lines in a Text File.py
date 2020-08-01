'''
Problem Description
The program takes the file name from the
user and counts number of lines in that file.
'''
print(__doc__)
print('-'*25)
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines %d: "%num_lines)