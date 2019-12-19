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
        if not n.left and n.right:
            return
        if n.left:
            self.heapify(n.left)
        if n.right:
            self.heapify(n.right)

        if n.left and is_valid(n.left, n) and (not n.right or is_valid(n.left, n.right)):
            tmp = n.value
            n.value = n.left.value
            n.left.value = tmp
        elif n.right and is_valid(n.right, n) and (not n.left or is_valid(n.right, n.left)):
            tmp = n.value
            n.value = n.right.value
            n.right.value = tmp

    def insert(self, value):
        l = "{0:b}".format(self.__len__()+1)
        if l == '1':
            self.root = HeapNode(value)
        else:
            tmp = self.root
            path = l[1:-1]
            final = l[-1]

            for i in path:
                if i == '0':
                    tmp = tmp.left
                else:
                    tmp = tmp.right

            if final == '0':
                tmp.left = HeapNode(value)
            else:
                tmp.right = HeapNode(value)
            self.heapify(self.root)

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        def len_node(n: HeapNode):
            if not n:
                return 0
            else:
                ll = len_node(n.left)
                lr = len_node(n.right)
                if lr > ll:
                    raise IndexError('Heap Broken')
                return 1 + ll + lr
        if self.root:
            return len_node(self.root)
        else:
            return 0


if __name__ == "__main__":
    a = Heap()
    for i in range(20):
        a.insert(i)