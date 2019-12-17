from hashlib import md5
from linked_list.linked_list import LinkedList

class HashTable():
    """
    Hash table with chaining method.
    Implemented by LinkedList
    """
    def __init__(self, hashTableSize: int=256):
        self.hashTableSize = hashTableSize
        self.buckets = [LinkedList() for x in range(0, hashTableSize)]

    def hash_key(self, key):
        sum_ = md5(str(key).encode('utf-8')).hexdigest()
        as_int = int(sum_,16)
        return as_int%(self.hashTableSize)

    def __repr__(self):
        s = ''
        for i in range(self.hashTableSize):
            if self.buckets[i].not_empty():
                s = s + str(i) + ": " + self.buckets[i].__repr__() + ',\n '
            else:
                continue
        if s != '':
            s = "{" + s[:-3]+ "}"
        else:
            s = "{}"
        return s
    
    def __setitem__(self, key: int, value):
        self.buckets[self.hash_key(value)].insert(value=value)
    
if __name__ == '__main__':
    a = HashTable(10)
    a['A'] = 'Apple'
    a['B'] = 'Banana'
    a['C'] = 'Cat'
    a['D'] = 'Dog'
    a['E'] = 'Egg'
    a['F'] = 'Frog'
    a['G'] = 'Goose'
    a['H'] = 'Hi'
    a['I'] = 'Ice'
    a['J'] = 'Juice'
    a['K'] = 'King'
    a['L'] = 'Lion'
    a['A2'] = 'Adam'
    a['B2'] = 'Bee'
    a['C2'] = 'Cow'
    a['D2'] = 'Duck'
    a['E2'] = 'Elephant'
    a['F2'] = 'Fun'
    a['G2'] = 'Girl'
    a['H2'] = 'Hello'
    a['I2'] = 'Ice-Cream'
    a['J2'] = 'Jump'
    a['K2'] = 'Kobe'
    a['L2'] = 'Lakers'
    print(a)
