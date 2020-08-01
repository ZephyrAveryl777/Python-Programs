'''
Discription:
-----------
__init__ would be treated as Constructor 
where as __call__ methods can be called 
with objects any number of times. Both 
__init__ and __call__ functions do take 
default arguments.
'''
print(__doc__)
print('-'*50)
class Counter:
    def __init__(self):
        self._weights = []
        for i in range(0, 2):
            self._weights.append(1)
        print(str(self._weights[-2]) + " No. from __init__")
 
    def __call__(self, t):
        self._weights = [self._weights[-1], self._weights[-1]
                         + self._weights[-1]]
        print(str(self._weights[-1]) + " No. from __call__")
 
 
num_count = Counter()
for i in range(0, 4):
    num_count(i)