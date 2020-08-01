'''
Problem Description
The program takes a string and creates 
a dictionary with key as first character 
and value as words starting with that character.

Problem Solution
1. Enter a string and store it in a variable.
2. Initialize a count variable to 0.
3. Create a set containing vowels.
4. Use a for loop to traverse through the letters in the string.
5. Using an if statement, check if the letter in the string is equal to a vowel.
6. If it is equal, increment the vowel count.
7. Print the final count of the vowels.
8. Exit.
'''
print('Count Number of vowels in string: ')
string=input('Enter string: ')
counter=0
vowels=set("aeiou")
vowel_letter=[] #used list here to specify the repeating vowels
for letter in string: 
	if letter in vowels:
		vowel_letter.append(letter)
		counter+=1
print(f'Count of vowels {vowel_letter} in string \'{string}\' is: {counter}')