import operator
from data_structure_sample.templates.complete_binary_tree import CompleteBinaryTree, CompleteBinaryTreeNode


class HeapNode(CompleteBinaryTreeNode):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return "HeapNode( "+self.value.__repr__()+" )"


class Heap(CompleteBinaryTree):
    def __init__(self, compare=operator.lt):
        if not (compare == operator.lt) and not (compare == operator.gt):
            raise TypeError('type should be either operator.lt or operator.gt')
        CompleteBinaryTree.__init__(self)
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
        CompleteBinaryTree.insert(self, HeapNode(value))
        self.heapify(self.root)
        return self

    def pop(self):
        if self.length <= 1:
            return super().pop().value
        value_root = self.root.value
        value_tail = super().pop().value
        if self.root:
            self.root.value = value_tail
        self.heapify(self.root)
        return value_root


if __name__ == '__main__':
    h = Heap(compare=operator.gt)
    for i in range(0, 7, 1):
        h.insert(i)

    h.preorder(h.root, print)
    #h.inorder(h.root, print)
    #h.postorder(h.root, print)

    for i in range(0, 70, 1):
        print(h.pop())
