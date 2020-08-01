'''
OOPS Descripiton:
----------------
Python is an object-oriented programming language. 
This means a Python programmer is able to take 
advantages of all pillars(Polymorphism, Inheritance, 
Abstraction, Encapsulation) of object oriented paradigm
The model of Object-Oriented Programming (OOP) is based 
on the concept of classes and objects.
'''
print(__doc__,end="")
print('-'*25)

#creating a class by using Class syntax
class Employee:
	name='John'
	age=26

#Creating Class Object:
e=Employee()
print(f'The name of the Employee is: {e.name} and age of employee is: {e.age}')
#print(type(e)) #this is to identify the type of 'e'

#Initializing the Object
'''The __init__() method is commonly known 
as an initializer method because it initializes 
the object's data attributes.'''
class Employee:
	def __init__(self,name,age):
		self.name=name
		self.age=age
e=Employee('Sam',36 )
print(f'The name of the Employee is: {e.name} and age of employee is: {e.age}')

#Object Method:
'''
A method is formatted identically to a function.
It starts with the def keyword, followed by a space, 
and the name of the method. Methods work in exactly the 
same way as simple functions, with one crucial exception: 
a method's first argument always receives the instance object. 
Those methods that do not take any arguments have at least the 
argument as self
'''
class Employee:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def details(self):
		print('Employee Name: ',self.name)
		print('Employee Age: ',self.age)

e=Employee('Tom', 25)
e.details()

#Self Parameter:
'''
The argument self is usually used to refer to object itself. 
When a method is called, Python makes the self parameter reference 
the specific object that the method is supposed to operate on.
'''
class Employee:
	def __init__(selfemployee,name,age):
		selfemployee.name=name
		selfemployee.age=age
	def details(selfemployee):
		print('Employee Name: ',selfemployee.name)
		print('Employee Age: ',selfemployee.age)

e=Employee('Mark', 34)
e.details()

#Delete Object and Property
'''
The del keyword allows to delete object or object property 
followed by object name.
'''
class Employee:
	def __init__(self,name,age):
		self.name=name
		self.age=age
e=Employee('Sam',23)
e1=Employee('MArk',34)
del e1
print(e)

#iterate over Object attributes
'''
Calling dir on the object gives you back 
all the attributes of that object, including 
python special attributes.
'''
class A():
    m = 1
    n = 2
 
    def __int__(self, x=1, y=2, z=3):
        self.x = x
        self._y = y
        self.__z__ = z
 
    def xyz(self):
        print(x, y, z)
 
obj = A()
print(dir(obj))
print([a for a in dir(obj) if not a.startswith('__')])

#printing all properties of an Object:
class Animal(object):
    def __init__(self):
        self.eyes = 2
        self.name = 'Dog'
        self.color= 'Spotted'
        self.legs= 4
        self.age  = 10
        self.kids = 0
 
 
animal = Animal()
animal.tail = 1
 
temp = vars(animal)
for item in temp:
    print(item, ':', temp[item])

#Create Data attributes of a class dynamically
'''
The setattr used to sets the named attribute on 
the given object with a specified value.'''
class Employee:
    pass
 
emp1 = Employee()
setattr(emp1, 'Salary', 12000)
 
emp2 = Employee()
setattr(emp2, 'Age', 25)
 
print(emp1.Salary)
print(emp2.Age)