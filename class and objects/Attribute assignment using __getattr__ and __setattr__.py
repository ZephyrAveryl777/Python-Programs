'''
Discription:
------------
The __getattr__ method intercepts attribute references 
and the __setattr__ intercepts all attribute assignments.
'''
print(__doc__,end="")
print('-'*55)
class Employee(object):
	def __init__(self,data):
		super().__setattr__('data',dict())
		self.data=data

	def __getattr__(self,name):
		if name in self.data:
			return self.data[name]
		else:
			return 0

	def __setattr__(self,key,value):
		if key in self.data:
			self.data[key]=value
		else:
			super().__setattr__(key, value)

e=Employee({'age' : 23,'name' : 'John' })
print('Details of the Employee:')
print('-'*25)
print(f'Age of the Employee is: {e.age}')
print(f'Name of Employee is: {e.name}')
print(f'Data of the Employee is: {e.data}')
print(f'Salary of the Employee is: {e.salary}')

e.salary=500000
print(f'Salary of the Employee after initalization is: {e.salary}')