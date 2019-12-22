from hashlib import md5
from linked_list.linked_list import LinkedList


class HashTable():
    """
    Hash table with chaining method.
    Implemented by LinkedList
    """

    def __init__(self, hashTableSize: int = 256):
        self.hashTableSize = hashTableSize
        self.buckets = [LinkedList() for x in range(0, hashTableSize)]

    def hash_key(self, key):
        sum_ = md5(str(key).encode('utf-8')).hexdigest()
        as_int = int(sum_, 16)
        return as_int % (self.hashTableSize)

    def __repr__(self):
        s = ''
        for i in range(self.hashTableSize):
            if self.buckets[i].not_empty():
                s = s + str(i) + ": " + self.buckets[i].__repr__() + ',\n '
            else:
                continue
        if s != '':
            s = "{" + s[:-3] + "}"
        else:
            s = "{}"
        return s

    def __setitem__(self, key: int, value):
        self.buckets[self.hash_key(value)].insert(value=value)
