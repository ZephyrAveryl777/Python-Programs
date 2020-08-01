print('Accessing private members in Class:')
print('-'*35)
class Human():
 
    # Private var
    __privateVar = "this is __private variable"
 
    # Constructor method
    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"
 
    # Public method
    def showName(self, name):
        self.name = name
        return self.__privateVar + " with name: " + name
 
    # Private method
    def __privateMethod(self):
        return "Private method"

    def _protectedMethod(self):
        return 'Protected Method'
 
    # Public method that returns a private variable
    def showPrivate(self):
        return self.__privateMethod()
 
    def showProtecded(self):
        return self._protectedMethod() 
 
 
class Male(Human):
    def showClassName(self):
        return "Male"
 
    def showPrivate(self):
        return self.__privateMethod()
 
    def showProtected(self):
        return self._protectedMethod()
 
 
class Female(Human):
    def showClassName(self):
        return "Female"
 
    def showPrivate(self):
        return self.__privateMethod()
 
 
human = Human()
print(f'\nCalling the: {human.className} from the Human class.')
print(f'\nAccessing the public method of Human class: {human.showName("Ling-Ling")}')
print(f'\nAccessing the private method of the Human class: {human.showPrivate()}, from Human Class.')
# print(f'Acessing the protected Method of the Human Class : {human.showProtected()},from Human Class.') -->AttributeError:'Human' object has no attribute 'showProtected'

male = Male()
print(f'\ncalling the {male.className} from the Male class')
print(f'\nAccessing the Public method of Male class: {male.showClassName()}, from male class')
print(f'\nAccessing the protected method of Male class: {male.showProtected()}, from male class.')
# print(f'Accessing the private method of Male class: {male.Human__showPrivate()}, from male Class.') --> AttributeError: 'Male' object has no attribute '_Male__privateMethod'

female = Female()
print(f'\ncalling the {female.className} from the Female class')
print(f'\nAccessing the Public method of female class: {female.showClassName()}, from Female class')
# print(f'Accessing the protected method of female class: {female.showProtected()}, from  Female class.') --> AttributeError: 'Female' object has no attribute 'showProtected'
# print(f'Accessing the private method of female class: {female.showPrivate()}, from Female Class.') AttributeError: 'Female' object has no attribute '_Female__privateMethod'

print('\n'+'-'*25+"Method 2 -- Accessing private members in Class"+'-'*25)
print('\n'+'Example: Public Attributes: ')
print('-'*20)
class Employee:
    def __init__(self,name,sal):
        self.name=name #Public attribute
        self.salary=sal #Public attribute
e1=Employee('Ling1',30000)
print(f'Accessing the Public Attributes: {e1.name} : {e1.salary}')

# if attribute is public then the value can be modified too
e1.salary=40000
print(f'Accessing the Public Attributes after modifying: {e1.name} : {e1.salary}')
print('\n'+'Example: Protected Attributes: ')
'''Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. 
This effectively prevents it to be accessed, unless it is from within a sub-class.'''
print('-'*25)
class Employee:
    def __init__(self,name,sal):
        self._name=name #protected attribute
        self._salary=sal #protected attribute
e2=Employee('Ling2',50000)
print(f'Accessing the Protected Attributes: {e2._name} : {e2._salary}')
#even if attribute is protected the value can be modified too
e2._salary=44000
print(f'Accessing the Protected Attributes after modifying: {e2._name} : {e2._salary}')
print('\n'+'Example: Private Attributes: ')
'''a double underscore __ prefixed to a variable makes it private. 
It gives a strong suggestion not to touch it from outside the class. 
Any attempt to do so will result in an AttributeError.'''
print('-'*25)
class Employee:
    def __init__(self,name,sal):
        self.__name=name  # private attribute 
        self.__salary=sal # private attribute
e3=Employee('Ling3',60000)
# print(f'Accessing the Privated Attributes: {e3.__name} : {e3.__salary}') --> AttributeError: 'Employee' object has no attribute '__name
'''In order to access the attributes, Python performs name mangling of private variables. 
Every member with double underscore will be changed to _object._class__variable.'''
print(f'Accessing the Private Attributes: {e3._Employee__name} : {e3._Employee__salary}')
#even if attribute is protected the value can be modified too
e3._Employee__salary=15000
print(f'Accessing the Protected Attributes after modifying: {e3._Employee__name} : {e3._Employee__salary}')

