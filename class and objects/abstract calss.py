'''
Discription:
------------
Abstract classes are classes that contain one or more abstract methods. 
An abstract method is a method that is declared, but contains no implementation. 
Abstract classes may not be instantiated, and require sub-classes to provide 
implementations for the abstract methods '''
from abc import ABC, abstractmethod
print(__doc__)
print('\n'+'-'*35+'Abstract Class'+'-'*35)
class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()
 
    @abstractmethod
    def eat(self):
        pass

class Parents(AbstractClass):
    def eat(self):
        return "Eat solid food " + str(self.value) + " times each day."
 
 
class Babies(AbstractClass):
    def eat(self):
        return "Drink Milk only " + str(self.value) + " times or more each day."
  
food = 3
adult = Parents(food)
print('Adult: ',end="")
print(adult.eat())
 
infant = Babies(food)
print('Infants: ',end="")
print(infant.eat())