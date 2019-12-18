class ListNode():
    """
    Node of a LinkedList.
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        return

    def __repr__(self):
        return self.value.__repr__()


class LinkedList():
    """
    Single linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, n: ListNode):
        if not self.head:
            self.head = n
            self.tail = n
            return
        else:
            self.tail.next = n
            self.tail = n
            return

    def insert(self, value):
        x = ListNode(value=value)
        self.insert_node(x)

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def not_empty(self):
        return (not self.is_empty())

    def __repr__(self):
        if not self.head:
            return '[]'
        x = self.head
        s = '['
        while(x):
            s = s + x.__repr__() + ', '
            x = x.next
        s = s[:-2] + "]"
        return s

    def __len__(self):
        if not self.head:
            return 0
        else:
            l = 1
            x = self.head
            while (x.next):
                x = x.next
                l += 1
            return l

    def __getitem__(self, key: int):
        try:
            l = self.__len__()
            x = self.head
            real_key = None
            if key >= l or (key < 0 and abs(key) > l):
                errmsg = 'list index out of range'
                raise IndexError(errmsg)
            elif key >= 0:
                real_key = key
            else:
                real_key = l + key
            while (real_key > 0):
                x = x.next
                real_key -= 1
            return x.value
        except:
            errmsg = 'list index out of range'
            raise IndexError(errmsg)

    def __setitem__(self, key: int, value):
        try:
            l = self.__len__()
            x = self.head
            real_key = None
            if key >= l or (key < 0 and abs(key) > l):
                errmsg = 'list index out of range'
                raise IndexError(errmsg)
            elif key >= 0:
                real_key = key
            else:
                real_key = l + key
            while (real_key > 0):
                x = x.next
                real_key -= 1
            x.value = value
        except:
            errmsg = 'list index out of range'
            raise IndexError(errmsg)


if __name__ == "__main__":
    a = LinkedList()
    print(a)
    a.insert('Apple')
    a.insert('Banana')
    a.insert('Cat')
    print("--------------")
    print(a)
