from siphash import siphash24


class DictionaryNode():
    """
    Node of a DictionaryLinkedList.
    """

    def __init__(self, key, value, me_hash):
        self.key = key
        self.value = value
        self.me_hash = me_hash
        self.collided = False

    def __repr__(self):
        return (self.key.__repr__() + ": " + self.value.__repr__())


class Dictionary():
    """
    Dictionary are implemented by HashTable
    Using open addressing method.
    Hash using siphash. I can not find siphash
    """

    def __init__(self):
        self.used_entry = 0
        self.buckets = [None for x in range(0, 8)]

    def me_hash(self, key):
        """
        hash of key
        """
        return siphash24(b'0123456789ABCDEF', (str(key).encode('utf-8'))).hash()

    def resize(self):
        """
        Change size if 
        1. load_factor > 2/3 or
        2. load_factor < 2/3
        return otherwise.
        """
        def proper_size(n):
            pro_size = 8 if n <= 2 else 2**(int(n * 1.5)).bit_length()
            return pro_size

        old_size = len(self.buckets)
        new_size = proper_size(self.used_entry)
        if old_size == new_size:
            return
        new_buckets = [None for x in range(0, new_size)]
        for i in range(old_size):
            if self.buckets[i] and (self.buckets[i].key is not None):
                entry = (self.buckets[i].me_hash) & (new_size-1)
                while new_buckets[entry]:
                    new_buckets[entry].collided = True
                    entry = entry+1 if entry < (new_size-2) else 0
                new_buckets[entry] = self.buckets[i]
                new_buckets[entry].collided = False
        self.buckets = new_buckets

    def __repr__(self):
        s = ''
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                s = s + self.buckets[i].__repr__() + ', '
        return "{}" if not s else "{{{0}}}".format(s[:-3])

    def __getitem__(self, key):
        l = len(self.buckets)
        entry = self.me_hash(key) & (l-1)
        while self.buckets[entry]:
            if self.buckets[entry].key == key:
                return self.buckets[entry].value
            if not self.buckets[entry].collided:
                raise KeyError(key)
            entry = entry+1 if entry < (l-2) else 0
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.used_entry += 1
        self.resize()
        l = len(self.buckets)
        key_me_hash = self.me_hash(key)
        entry = key_me_hash & (l-1)
        while self.buckets[entry]:
            self.buckets[entry].collided = True
            entry = entry+1 if entry < (l-2) else 0
        self.buckets[entry] = DictionaryNode(key=key,
                                             value=value,
                                             me_hash=key_me_hash)

    def __delitem__(self, key):
        key_me_hash = self.me_hash(key)
        l = len(self.buckets)
        entry = key_me_hash & (l-1)
        while self.buckets[entry]:
            if self.buckets[entry].key == key:
                self.buckets[entry].key = None
                self.buckets[entry].value = None
                self.buckets[entry].me_hash = None
                return
            if not self.buckets[entry].collided:
                raise KeyError(key)
            entry = entry+1 if entry < (l-2) else 0
        raise KeyError(key)

    def __len__(self):
        counter = 0
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                counter += 1
        return counter
