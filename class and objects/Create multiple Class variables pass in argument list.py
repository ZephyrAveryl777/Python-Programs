'''
Discription: 
-----------
Create multiple Class variables pass in argument list'''
print(__doc__)
print('-'*50)
class Employee(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key]) 
emp = Employee(age=25, name="John Doe")
print(emp.age)
print(emp.name)