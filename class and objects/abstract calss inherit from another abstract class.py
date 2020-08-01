'''
A class that is derived from an abstract class cannot be 
instantiated unless all of its abstract methods are overridden.
'''
from abc import ABC,abstractmethod
print(__doc__,end="")
print('\n'+'-'*25+'Abstract class inherit from another abstract class'+'-'*35)
class A(ABC):
	def __init__(self,username):
		self.username=username
		super().__init__()

	@abstractmethod
	def name(self):
		pass
class B(A):
	@abstractmethod
	def age(self):
		pass

class C(B):
	def name(self):
		print(self.username)

	def age(self):
		return

c=C('Testing-123456')
c.name()