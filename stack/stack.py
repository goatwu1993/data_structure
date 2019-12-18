class Stack():
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)
        return self

    def pop(self):
        if not self.items:
            raise IndexError('pop from empty list')
        tmp = self.items[-1]
        self.items = self.items[:-1]
        return tmp

    def __repr__(self):
        return "Stack("+self.items.__repr__()+")"


if __name__ == '__main__':
    a = Stack()
    print(a)
    a.append('a')
    a.append('apple')
    print(a)
    a.pop()
    print(a)
    a.pop()
    print(a)
    a.append('b')
    a.append('bob')
    print(a)
    print(a.pop())
    print(a.pop())
    print(a)
