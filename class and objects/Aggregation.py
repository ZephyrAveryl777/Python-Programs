'''
Discription:
------------
Aggregation is a week form of composition. 
If you delete the container object contents 
objects can live without container object.
'''
print(__doc__,end="")
print('-'*35)
class Salary:
	def __init__(self,pay):
		self.pay=pay

	def get_total(self):
		return (self.pay*12)

class Employee:
	def __init__(self,pay,bonus):
		self.pay=pay
		self.bonus=bonus

	def annual_salary(self):
		return str(self.pay.get_total() + self.bonus)

obj_sal = Salary(600)
obj_employee = Employee(obj_sal, 500)
print(f'Total Salary of the Employee is: {obj_employee.annual_salary()}')