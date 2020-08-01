'''
Description:
------------
Iterables can implement __reversed__ to return 
an iterator that goes backwards.
'''
print(__doc__,end="")
print('-'*25)
class Count:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = None
 
    def __iter__(self):
        self.current = self.start
        while self.current < self.end:
            yield self.current
            self.current += 1
 
    def __next__(self):
        if self.current is None:
            self.current = self.start
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current-1
 
    def __reversed__(self):
        self.current = self.end
        while self.current >= self.start:
            yield self.current
            self.current -= 1
 
 
obj1 = Count(0,6)
for i in obj1:
    print(i)
print('-'*20)
obj2 = reversed(obj1)
for i in obj2:
    print(i)
 