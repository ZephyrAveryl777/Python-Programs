'''
Problem Description
The program takes two dictionaries and 
concatenates them into one dictionary.

Problem Solution
1. Declare and initialize two dictionaries 
with some key-value pairs
2. Use the update() function to add the 
key-value pair from the second dictionary 
to the first dictionary.
3. Print the final dictionary.
4. Exit.
'''
d1={'A': 1,'B': 2}
d2={'C': 3}
d1.update(d2)
print(f'First dictionary is: {d1}\nSecon dictionary is: {d2}\nConcatenated dictionary is: {d1}')