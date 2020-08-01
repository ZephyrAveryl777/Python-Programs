class Counter(object):
    def __init__(self, floors):
        self._floors = [None]*floors
 
    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data
 
    def __getitem__(self, floor_number):
        return self._floors[floor_number]
 
 
index = Counter(4)
index[0] = 'ABCD'
index[1] = 'EFGH'
index[2] = 'IJKL'
index[3] = 'MNOP'
 
print(index[2])