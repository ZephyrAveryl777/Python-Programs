'''
Discription:
------------
The __del__ is a finalizer. It is called when an object 
is garbage collected which happens at some point after 
all references to the object have been deleted.
'''
print(__doc__,end="")
print('-'*45)
class Employee():
	def __init__(self,name='John Doe'):
		print('Hello '+ name)
		self.name=name

	def developer(self):
		print(self.name)

	def __del__(self):
		print('Good Bye '+self.name)

e=Employee('Mark')
print(f'Data of the employee is defined at: {e}')
e='Rock'
print(f'Data of the user after using __del__: {e}')