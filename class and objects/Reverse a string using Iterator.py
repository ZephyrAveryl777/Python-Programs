'''
Discription:
------------
Iterators implement a __next__ method that returns 
individual items, and a __iter__ method that returns self .

Problem Statement: 
------------------
Reverse string using Iterator.
'''
print(__doc__,end='')
print('-'*30)
class Reverse:
	def __init__(self,data):
		self.data=data
		self.index=len(data)
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.index==0:
			raise StopIteration
		self.index=self.index-1
		return self.data[self.index]

test=Reverse(input('Enter your text here: '))
print('Text after reversing is:  ',end="")
for char in test:
	print(char,end="")

