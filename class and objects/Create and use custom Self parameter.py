'''
self is an object reference to the object itself, 
it does not have to be named self , but it has to 
be the first parameter of any function in the class.
'''
class Employee:
	def __init__(person,salary,name):
		person.salary=salary
		person.name=name

	def printDetails(e):
		print(f'{e.salary} : {e.name}')

e=Employee(1000, 'John')
e.printDetails()