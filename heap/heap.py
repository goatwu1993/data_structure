import operator
    

class HeapNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "HeapNode( "+self.value.__repr__()+" )"


class Heap():
    def __init__(self, compare=operator.lt):
        if not (compare == operator.lt) and not (compare == operator.gt):
            raise TypeError('type should be either operator.lt or operator.gt')
        self.root = None
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
        def insert_not_full(n: HeapNode, d: int, v):
            if not d:
                self.root = HeapNode(value)
                return True
            if d == 1:
                return False
            if d == 2 and not n.left:
                n.left = HeapNode(v)
                return True
            if d == 2 and not n.right:
                n.right = HeapNode(v)
                return True
            return (insert_not_full(n.left, d-1, v) or insert_not_full(n.right, d-1, v))

        if not insert_not_full(self.root, self.depth(), value):
            # The heap is currently full (all branch have same depth)
            pos = self.root
            while pos.left:
                pos = pos.left
            pos.left = HeapNode(value)
        self.heapify(self.root)
        return self

    def depth(self):
        if not self.root:
            return 0
        rs, pos = 1, self.root
        while pos.left:
            rs, pos = rs+1, pos.left
        return rs

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
    h = Heap(compare=operator.gt)
    for i in range(0, 20, 1):
        h.insert(i)

    for i in range(0, 10, 1):
        h.insert(i)
