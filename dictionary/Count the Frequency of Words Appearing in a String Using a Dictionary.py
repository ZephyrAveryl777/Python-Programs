'''
Problem Description
The program takes a string and counts the frequency of words appearing in that string using a dictionary.

Problem Solution
1. Enter a string and store it in a variable.
2. Declare a list variable and initialize it to an empty list.
3. Split the string into words and store it in the list.
4. Count the frequency of each word and store it in another list.
5. Using the zip() function, merge the lists containing the words and the word counts into a dictionary.
3. Print the final dictionary.
4. Exit.
'''
Text=input('Enter string: ')
l=[]
l=Text.split()
wordcounter=[l.count(p) for p in l]
print(dict(zip(l,wordcounter)))