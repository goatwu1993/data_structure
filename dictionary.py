from hash_table import HashTable
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
        self.bitmask = 3
        self.buckets = [None for x in range(0, 8)]

    def me_hash(self, key):
        """
        I dont know how to use byte in Python
        Store the hash sum as int instead
        """
        hex_int = siphash24(b'0123456789ABCDEF',
                            (str(key).encode('utf-8'))).hash()
        return hex_int

    def resize(self):
        """
        Should change the size if load_factor > 2/3 or load_factor < 2/3
        Should do nothing if load_factor between 1/3 and 2/3
        """
        used = self.used_entry
        l = proper_size = len(self.buckets)
        load_factor = used/l
        if load_factor > 1/3 and load_factor < 2/3:
            return
        if load_factor < 1/3 and l == 8:
            return
        if load_factor >= 2/3:
            while load_factor > 2/3:
                proper_size *= 2
                load_factor = used/proper_size
        elif load_factor <= 1/3:
            while load_factor < 1/3:
                proper_size /= 2
                load_factor = used/proper_size
        else:
            raise IndexError('load factor:', load_factor, 'out of control')

        new_buckets = [None for x in range(0, proper_size)]
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                key_me_hash = self.buckets[i].me_hash
                entry = key_me_hash % proper_size
                while new_buckets[entry]:
                    new_buckets[entry].collided = True
                    if entry < proper_size - 2:
                        entry += 1
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
        if not s:
            return "{}"
        else:
            return "{" + s[:-3] + "}"

    def __getitem__(self, key):
        key_me_hash = self.me_hash(key)
        l = len(self.buckets)
        entry = key_me_hash % l
        while self.buckets[entry]:
            if self.buckets[entry].key == key:
                return self.buckets[entry].value
            elif not self.buckets[entry].collided:
                raise KeyError(key)
            elif entry < l-2:
                entry += 1
            else:
                entry = 0
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.used_entry += 1
        self.resize()
        self.used_entry = self.__len__()

        l = len(self.buckets)
        key_me_hash = self.me_hash(key)
        entry = key_me_hash % l
        while self.buckets[entry]:
            self.buckets[entry].collided = True
            if entry < l-2:
                entry += 1
            else:
                entry = 0
        self.buckets[entry] = DictionaryNode(key=key,
                                             value=value,
                                             me_hash=key_me_hash)

    def __delitem__(self, key):
        key_me_hash = self.me_hash(key)
        l = len(self.buckets)
        entry = key_me_hash % l
        while self.buckets[entry]:
            if self.buckets[entry].key == key:
                self.buckets[entry].key = None
                self.buckets[entry].value = None
                self.buckets[entry].me_hash = None
                return
            elif not self.buckets[entry].collided:
                raise KeyError(key)
            elif entry < l-2:
                entry += 1
            else:
                entry = 0
        raise KeyError(key)

    def __len__(self):
        counter = 0
        for i in range(len(self.buckets)):
            if self.buckets[i]:
                counter += 1
        return counter


def get(key):
    entry = me_hash(key)
    while is_valid(entry)
       if hash_table[entry] == None:
            # 這個Entry從來沒有被使用過
            raise IndexError('key not exist')
        if hash_table[entry] and \
                hash_table[entry].key != key and \
                not hash_table[entry].collided:
            # 此entry已經有值，但key不對，但沒有發生過collided=>
            # 只是剛好entry相同，且沒發生collide，直接返回indexError即可
            raise IndexError('key not exist')
        if hash_table[entry] and \
                hash_table[entry].key != key and \
                hash_table[entry].collided:
            # 此entry已經有值，但key不對，但有發生過collided =>
            # 往下查找
            entry += 1
        if hash_table[entry] and \
            not hash_table[entry].key and \
            not hash_table[entry].value and
        hash_table[entry].collided:
            # 此Node被del，但為了提示之後要往後查找，流下 collided 屬性。
            entry += 1
        if hash_table[entry] and hash_table[entry].key == key:
            return Dictionary[entry].value
