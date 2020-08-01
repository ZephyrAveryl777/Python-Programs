'''
Discription: 
-----------
Variables declared inside the class definition, 
but not inside a method are  static variables.
'''
print(__doc__,end="")
print('-'*40)
class Employee:
	age=25

print(f'Employee age is: {Employee.age}')#25
e=Employee()
print(f'Employee age is: {e.age}')#25

e.age=30
print(f'Employee age is: {Employee.age}')#25
print(f'Employee age after reassigning is: {e.age}')#30