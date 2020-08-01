'''
Description: 
------------
When objects are instantiated, the object itself 
is passed into the self parameter. The Object is 
passed into the self parameter so that the object 
can keep hold of its own data.
'''
print(__doc__)
print('-'*25)

class State(object):
    def __init__(self):
       global x 
       x=self.field = 5.0
 
    def add(self, x):
        self.field += x
 
    def mul(self, x):
        self.field *= x
 
    def div(self, x):
        self.field /= x
 
    def sub(self, x):
        self.field -= x

n=int(input('Enter a valued: '))

s = State()
print(f"\nAfter intializing the varaiable, the value of variable is: {s.field}")
 
s.add(n)         # Self is implicitly passed.
print(f"\nAddition of the initalized variable {x} with {n} is: {s.field}")
 
s.mul(n)         # Self is implicitly passed.
print(f"\nMultiplication of the initalized variable {x} with {n} is: {s.field}")
 
s.div(n)         # Self is implicitly passed.
print(f"\nSubtraction of the initalized variable {x} with {n} is: {s.field}")
 
s.sub(n)         # Self is implicitly passed.
print(f"\nDivision of the initalized variable {x} with {n} is: {s.field}")