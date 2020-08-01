'''
A metaclass is the class of a class. 
A class defines how an instance of the class 
(i.e. an object) behaves while a metaclass defines 
how a class behaves. A class is an instance of a metaclass. 
A metaclass is most commonly used as a class-factory. 
When you create an object by calling the class, Python creates 
a new class (when it executes the 'class' statement) by calling 
the metaclass. However, metaclasses actually define the type of a 
class, not just a factory for it, so you can do much more with them.
'''
print(__doc__)
print('-'*50)
def _addMethod(fldName, clsName, verb, methodMaker, dict):
    compiledName = _getCompiledName(fldName, clsName)
    methodName = _getMethodName(fldName, verb)
    dict[methodName] = methodMaker(compiledName)
 
 
def _getCompiledName(fldName, clsName):
    if fldName[:2] == "__" and fldName[-2:] != "__":
        return "_%s%s" % (clsName, fldName)
    else:
        return fldName
 
 
def _getMethodName(fldName, verb):
    s = fldName.lstrip("_")
    return verb + s.capitalize()
 
 
def _makeGetter(compiledName):
    return lambda self: self.__dict__[compiledName]
 
 
def _makeSetter(compiledName):
    return lambda self, value: setattr(self, compiledName, value)
 
 
class Accessors(type):
    def __new__(cls, clsName, bases, dict):
        for fldName in dict.get("_READ", []) + dict.get("_READ_WRITE", []):
            _addMethod(fldName, clsName, "get", _makeGetter, dict)
        for fldName in dict.get("_WRITE", []) + dict.get("_READ_WRITE", []):
            _addMethod(fldName, clsName, "set", _makeSetter, dict)
        return type.__new__(cls, clsName, bases, dict)
 
 
class Employee(object, metaclass=Accessors):
    _READ_WRITE = ['name', 'salary', 'title', 'bonus']
 
    def __init__(self, name, salary, title, bonus=0):
        self.name = name
        self.salary = salary
        self.title = title
        self.bonus = bonus
 
 
b = Employee('John Doe', 25000, 'Developer', 5000)
print('Name:', b.getName())
print('Salary:', b.getSalary())
print('Title:', b.getTitle())
print('Bonus:', b.getBonus())