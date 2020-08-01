print('''
The task here is to remove all the white-spaces 
from the string. For this purpose, we need to 
traverse the string and check if any character 
of the string is matched with a white-space 
character or not. If so, Use any built-in method 
like replace() with a blank.
''')
string=input('Enter string here: ')
#using in-built function in python
#Here, replace space character with blank
string=string.replace(" ","")
print(f'String after removing all the white spaces: \"{string}\"')