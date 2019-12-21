import operator


class HeapNode():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.left = None

    def __repr__(self):
        return "HeapNode( "+self.value.__repr__()+" )"


class Heap():
    def __init__(self, compare=operator.lt):
        if not (compare == operator.lt) and not (compare == operator.gt):
            raise TypeError('type should be either operator.lt or operator.gt')
        self.root = None
        self.length = 0
        self.compare = compare

    def heapify(self, n: HeapNode):
        if not n:
            return
        compare = self.compare
        self.heapify(n.left)
        self.heapify(n.right)
        if n.left and compare(n.left.value, n.value) and (not n.right or compare(n.left.value, n.right.value)):
            n.value, n.left.value = n.left.value, n.value
        elif n.right and compare(n.right.value, n.value) and (not n.left or compare(n.right.value, n.left.value)):
            n.value, n.right.value = n.right.value, n.value

    def insert(self, value):
        if not self.length:
            self.root = HeapNode(value)
            self.length += 1
        l = bin(self.length + 1)
        path = bin(self.length + 1)[3:-1]
        final = bin(self.length + 1)[-1]
        pos = self.root
        position = self.root
        for i in path:
            pos = pos.left if i == '0' else pos.right
        if final == '0':
            pos.left = HeapNode(value)
        else:
            pos.right = HeapNode(value)
        self.length += 1
        self.heapify(self.root)
        return self

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        return self.length


if __name__ == '__main__':
    h = Heap(compare=operator.gt)
    for i in range(0, 20, 1):
        h.insert(i)

    for i in range(0, 10, 1):
        h.insert(i)
