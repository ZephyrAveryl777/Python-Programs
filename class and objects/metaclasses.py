'''
Discription: 
------------
Metaclass allows you to separate what the class does from the details of 
how its created. The metaclass and class are each responsible for one thing. 
You can write the code once in a metaclass, and use it for customizing several 
classes call behavior without worrying about multiple inheritance. Subclasses 
can override behavior in their __new__ method, but __call__ on a metaclass doesnot 
have to even call __new__ at all. If there is setup work, you can do it in the __new__ method 
 of the metaclass, and it only happens once, instead of every time the class is called.'''
print(__doc__)
print('\n'+'-'*35+'MetaClass in python'+'-'*35)
class UpperAttrNameMetaClass(type):
        def __new__(cls, clsname, bases, attrdict, *args, **kwargs):
                print('1. Create a new type, from ' +
                      ' UpperAttrNameMetaClass.__new__')
                new_attrs = dict()
                for attr, value in attrdict.items():
                        if not callable(value) and not str(attr).startswith('__'):
                                new_attrs[attr.upper()] = value
                        else:
                                new_attrs[attr] = value
 
                cls_obj = super().__new__(cls, clsname, bases, new_attrs,
                                          *args, **kwargs)
                return cls_obj
 
        def __init__(self, clsname, bases, attrdict):
                self.test = 'test'
                super().__init__(clsname, bases, attrdict)
                print('2. Initialize new type, increase test attribute,' +
                      'from UpperAttrNameMetaClass.__init__')
 
        def __call__(self, *args, **kwargs):
                print('3. Instantiate the new class,' +
                      ' from UpperAttrNameMetaClass.__call__')
                new_obj = self.__new__(self, *args, **kwargs)
                new_obj.__init__(*args, **kwargs)
                return new_obj
 
 
class ObjectNoInitMetaClass(type):
        def __call__(cls, *args, **kwargs):
                if len(args):
                        raise TypeError('Must use keyword argument ' +
                                        ' for key function')
                new_obj = cls.__new__(cls)
                for k, v in kwargs.items():
                        setattr(new_obj, k.upper(), v)
                return new_obj
 
 
class Pig(object, metaclass=UpperAttrNameMetaClass):
        size = 'Big'
 
        def __new__(cls, *args, **kwargs):
                print('4. Call __new__ in the __call__ of the metaclass,' +
                      ' from Pig.__new__')
                obj = object.__new__(cls)
                return obj
 
        def __init__(self):
                print('5. After the new object is instantiated in ' +
                      'the __call__ of the metaclass,the object is promoted,' +
                      ' from Pig.__init__')
                self.name = 'Mark'
 
        def talk(self):
                print(self.name)
 
 
Pig().talk()
print(Pig.__dict__)
print(Pig.SIZE)
 
 
class AnyOne(metaclass=ObjectNoInitMetaClass):
        pass
 
 
foo = AnyOne(name='John', age=28)
print(foo.NAME, foo.AGE)
print(foo.__dict__)
