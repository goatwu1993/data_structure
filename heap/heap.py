class HeapNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "HeapNode( "+self.value.__repr__()+" )"


class Heap():
    def __init__(self, type: str = 'Max'):
        if not (type == 'Min') and not (type == 'Max'):
            raise TypeError('type should be either Min or Max')
        self.type = type
        self.root = None

    def heapify(self, n: HeapNode):
        def is_valid(node1: HeapNode, node2: HeapNode):
            if self.type == 'Min':
                return node1.value < node2.value
            else:
                return node1.value > node2.value
        if not n:
            return
        self.heapify(n.left)
        self.heapify(n.right)
        if n.left and is_valid(n.left, n) and (not n.right or is_valid(n.left, n.right)):
            n.value, n.left.value = n.left.value, n.value
            return
        elif n.right and is_valid(n.right, n) and (not n.left or is_valid(n.right, n.left)):
            n.value, n.right.value = n.right.value, n.value
            return

    def insert(self, value):
        l = "{0:b}".format(self.__len__()+1)
        if l == '1':
            self.root = HeapNode(value)
            return self
        pos = self.root
        path = l[1:-1]
        final = l[-1]
        # traverse through heap
        for i in path:
            pos = (pos.left if i == '0' else pos.right)
        # final assign
        if final == '0':
            pos.left = HeapNode(value)
        else:
            pos.right = HeapNode(value)
        self.heapify(self.root)
        return self

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        def len_node(n: HeapNode):
            if not n:
                return 0
            ll, lr = len_node(n.left), len_node(n.right)
            if lr > ll:
                raise IndexError('Heap Broken')
            return 1 + ll + lr
        return len_node(self.root)


if __name__ == "__main__":
    a = Heap()
    for i in range(20):
        a.insert(i)
