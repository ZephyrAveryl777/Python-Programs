'''
Problem Description
The program takes a string and determines how many times a given letter occurs in a string recursively.

Problem Solution
1. Take a string and a character from the user and store it in different variables.
2. Pass the string and the characters as arguments to a recursive function.
3. Pass the base condition that the string isn’t empty.
4. Check if the first character of the string is equal to the character taken from the user and if it is equal, increment the count.
5. Progress the string either wise and print the number of times the letter occurs in the string.
6. Exit.
'''
def check(string,ch):
      if not string: # if character not in string
        return 0 # return 0 as count
      elif string[0]==ch: # checking whether the first character of string and given character are same or not
            return 1+check(string[1:],ch) # iterate through the characters of the string
      else:
            return check(string[1:],ch) #if found at first position then return the value 
string=input("Enter string:")
ch=input("Enter character to check:")
print(f"Count of {ch} in \'{string}\' is: {check(string,ch)}")
