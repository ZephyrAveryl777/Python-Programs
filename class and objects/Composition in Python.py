'''
Discription:
------------
In composition one of the classes is composed of one or 
more instance of other classes. In other words one class 
is container and other class is content and if you delete 
the container object then all of its contents objects are also deleted.
'''
print(__doc__,end="")
print('-'*55)
class Salary:
    def __init__(self, pay):
        self.pay = pay
 
    def get_total(self):
        return (self.pay*12)
 
 
class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)
 
    def annual_salary(self):
        return str(self.obj_salary.get_total() + self.bonus)
  
obj_emp = Employee(600, 500)
print(f'Total Salary of the employee is: {obj_emp.annual_salary()}')
