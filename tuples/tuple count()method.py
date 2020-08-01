'''
You can use count() method to 
calculate the number of times a 
specified value appears in the tuple.
'''
test = ("Canada", "America", "Canada", "Japan", "Italy", "Canada")
print(f'Elements of tuple: {test}')
word=input('Enter the word to be counted in the tuple: ') 
num = test.count(word)
 
print(f'Counting the occurance of word {word} is: {num}')