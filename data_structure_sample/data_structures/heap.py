import operator


class Heap():
    def __init__(self, compare=operator.lt):
        self.items = []
        self.compare = compare

    def heapify(self):
        def swap(i):
            l = len(self.items)
            if 2*i + 2 > l:
                return
            compare = self.compare
            if compare(self.items[2*i+1], self.items[i]):
                self.items[2*i+1], self.items[i] = self.items[i], self.items[2*i+1]
            if ((2*i+2 < l)
                    and compare(self.items[2*i+2], self.items[i])):
                self.items[2*i+2], self.items[i] = self.items[i], self.items[2*i+2]
        l = len(self.items)

        for i in reversed(range(l//2)):
            swap(i)

    def insert(self, index, value):
        self.items.insert(index, value)
        self.heapify()
        return self

    def append(self, value):
        self.items.append(value)
        self.heapify()
        return self

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty list")
        rs = self.items.pop(0)
        self.items = self.items[1:]+[self.items[0]]
        self.heapify()
        return rs

    def __repr__(self):
        return self.items.__repr__()

    def __setitem__(self, key, value):
        self.items[key] = value
        self.heapify()

    def __getitem__(self, key):
        return self.items[key]

    def __delitem__(self, key):
        del self.items[key]
        self.heapify()

    def __len__(self):
        return self.items.__len__()

