'''
Discription:
-----------
The __iter__ returns the iterator object and is implicitly called 
at the start of loops. The __next__ method returns the next value 
and is implicitly called at each loop increment. __next__ raises 
a StopIteration exception when there are no more value to return, 
which is implicitly captured by looping constructs to stop iterating.
'''
print(__doc__,end='')
print('-'*50)
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
 
 
for num in Counter(5, 15):
    print(num)