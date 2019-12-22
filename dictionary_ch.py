from hash_table import HashTable
from linked_list import LinkedList, ListNode


class DictionaryNode(ListNode):
    """
    Node of a DictionaryLinkedList.
    """

    def __init__(self, key, value, me_hash=0):
        self.key = key
        self.me_hash = me_hash
        super().__init__(value=value)

    def __repr__(self):
        return (self.key.__repr__() + ": " + self.value.__repr__())


class DictionaryLinkedList(LinkedList):
    """
    Single linked list with a key for Dictionary.
    """

    def exist(self, key):
        if not self.head:
            return True
        else:
            x = self.head
            while x.key != key:
                if x.next:
                    x = x.next
                else:
                    return False
            return True

    def not_exist(self, key):
        return not self.exist(key)

    def __repr__(self):
        if not self.head:
            return
        x = self.head
        s = '['
        while(x):
            s = s + x.__repr__() + ', '
            x = x.next
        s = s[:-2] + "]"
        return s

    def __getitem__(self, key):
        n = self.head
        while n and (n.key != key):
            n = n.next
        if not n:
            raise IndexError
        else:
            return n.value

    def __setitem__(self, key, value):
        if not self.head:
            n = DictionaryNode(key, value)
            self.head = n
            self.tail = n
        else:
            x = self.head
            while x.key != key:
                if x.next:
                    x = x.next
                else:
                    x = None
                    break
            if x:
                x.value = value
            else:
                n = DictionaryNode(key, value)
                self.tail.next = n
                self.tail = n


class Dictionary(HashTable):
    """
    Dictionary are implemented by HashTable
    """

    def __init__(self, hashTableSize: int = 256):
        self.hashTableSize = hashTableSize
        self.buckets = [DictionaryLinkedList()
                        for x in range(0, hashTableSize)]

    def __getitem__(self, key):
        return(self.buckets[self.hash_key(key)][key])

    def __setitem__(self, key, value):
        self.buckets[self.hash_key(key)][key] = value
