'''
Making the __init__ an abstract method
'''
from abc import ABCMeta, abstractmethod
print(__doc__,end="")
print('\n'+'-'*35+'Abstract Class to override default constructor'+'-'*35)
class AbstractClass(object,metaclass=ABCMeta):
	@abstractmethod
	def __init__(self,n):
		self.n=n

class Employee(AbstractClass):
	def __init__(self,salary,name):
		self.salary=salary
		self.name=name

e1=Employee(1000,'John Doe')
print(f'Salary of the Employee: {e1.salary} and name of the Employee: {e1.name}')
