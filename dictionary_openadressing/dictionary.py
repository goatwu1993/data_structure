from hash_table.hash_table import HashTable
from hashlib import md5
from linked_list.linked_list import LinkedList, ListNode
import struct

class DictionaryNode():
    """
    Node of a DictionaryLinkedList.
    """
    def __init__(self, key, value, hash_int=0):
        self.key = key
        self.value = value
        self.hash_int = hash_int
        self.collided = False
    
    def __repr__(self):
        return ( self.key.__repr__() + ": " + self.value.__repr__())

class Dictionary():
    """
    Dictionary are implemented by HashTable
    Using open addressing method.
    Hash using md5. I can not find siphash
    """
    def __init__(self):
        self.used_entry = 0
        self.bitmask = 3
        self.buckets = [ None for x in range(0, 8) ]

    def hash_int(self, key):
        """
        I dont know how to use byte in Python
        Store the hash sum as int instead
        """
        hex_int = int(md5(str(key).encode('utf-8')).hexdigest(),16)
        return hex_int
    
    def resize(self):
        """
        Should change the size if used > 2/3 or used < 2/3
        Should do nothing if used between 1/3 and 2/3
        """
        used = self.used_entry
        l = proper_size = len(self.buckets)
        used_percentage = used/l
        if used_percentage > 1/3 and used_percentage < 2/3:
            return 
        elif used_percentage < 1/3 and l == 8:
            return
        elif used_percentage >= 2/3:
            while used_percentage > 2/3:
                proper_size *= 2
                used_percentage = used/proper_size
        elif used_percentage <= 1/3:
            while used_percentage < 1/3:
                proper_size /= 2
                used_percentage = used/proper_size

        new_buckets = [ None for x in range(0, proper_size) ]
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                key_hash_int = self.buckets[i].hash_int
                entry = key_hash_int % proper_size
                while new_buckets[entry]:
                    new_buckets[entry].collided = True
                    if entry < proper_size - 2:
                        entry+=1
                    else:
                        entry = 0
                new_buckets[entry] = self.buckets[i]
                new_buckets[entry].collided = False
        self.buckets = new_buckets
        return

    def __repr__(self):
        s = ''
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                s = s + self.buckets[i].__repr__() + ', '
        if not s :
            return "{}"
        else:
            return "{" + s[:-3]+ "}"
    
    def __getitem__(self, key):
        key_hash_int = self.hash_int(key)
        l = len(self.buckets)
        entry = key_hash_int % l
        while self.buckets[entry]:
            if self.buckets[entry].key == key:
                return self.buckets[entry].value
            elif not self.buckets[entry].collided:
                raise KeyError(key)
            elif entry < l-2:
                entry+=1
            else:
                entry = 0
        raise KeyError(key)
        
    
    def __setitem__(self, key, value):
            
        self.used_entry += 1
        self.resize()
        self.used_entry = self.__len__()
        
        l = len(self.buckets)
        key_hash_int = self.hash_int(key)
        entry = key_hash_int % l
        while self.buckets[entry]:
            self.buckets[entry].collided = True
            if entry < l-2:
                entry+=1
            else:
                entry = 0
        self.buckets[entry] = DictionaryNode(key = key,
            value=value,
            hash_int=key_hash_int)
    
    def __delitem__(self, key):
        key_hash_int = self.hash_int(key)
        l = len(self.buckets)
        entry = key_hash_int % l
        while self.buckets[entry]:
            if self.buckets[entry].key == key:
                self.buckets[entry].key = None
                self.buckets[entry].value = None
                self.buckets[entry].hash_int = None
                return
            elif not self.buckets[entry].collided:
                raise KeyError(key)
            elif entry < l-2:
                entry+=1
            else:
                entry = 0
        raise KeyError(key)
    
    def __len__(self):
        counter = 0
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                counter += 1
        return counter

        
    