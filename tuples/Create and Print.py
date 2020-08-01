'''
Python tuple is a sequence, 
which can store heterogeneous data
types such as integers, floats, strings, 
lists, and dictionaries. Tuples are written 
with round brackets and individual objects 
within the tuple are separated by a comma. 
The two biggest differences between a tuple
and a list are that a tuple is immutable 
and allows you to embed one tuple inside another.

There are many ways to input values 
into the tuple most of them are not so 
friendly and here goes the easilest one 
'''
a=[]
n=int(input('Enter size of tuple: ')) 
for i in range(n):
	a.append(int(input('Enter Element: ')))

print(f'\nElements of the variable are: {a}')
print(f'Type of what we created is: {type(a)}')
a=tuple(a)
print(f'\nElements of the tuple are: {a}')
print(f'Type of what we created is: {type(a)}')

#other ways to create and print Tuples:
tuple1 = ()   # An empty tuple.
tuple2 = (1, 2, 3)  # A tuple containing three integer objects.
 
# A tuple containing  string objects.
tuple3 = ("America", "Israel","Canada", "Japan")
 
# A tuple containing an integer, a string, and a boolean object.
tuple4 = (100, "Italy", False)
 
# A tuple containing another tuple.
tuple5 = (50, ("America", "Canada", "Japan"))
 
# The extra comma, tells the parentheses are used to hold a singleton tuple.
tuple6 = (25,)
 
print(f'\n Empty tuple: {tuple1}')
print(f'\n Tuple containing three integer objects: {tuple2}')
print(f'\n Tuple containing  string objects: {tuple3}')
print(f'\n Tuple containing an integer, a string, and a boolean objects: {tuple4}')
print(f'\n Tuple containing another tuple: {tuple5}')
print(f'\n Tuple containing  singleton object: {tuple6}')
