class CompleteBinaryTreeNode():
    def __init__(self):
        self.left = None
        self.right = None


class CompleteBinaryTree():
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, node):
        if not self.length:
            self.root = node
            self.length += 1
            return self
        path = bin(self.length + 1)[3:-1]
        final = bin(self.length + 1)[-1]
        pos = self.root
        for i in path:
            pos = pos.left if i == '0' else pos.right
        if final == '0':
            pos.left = node
        else:
            pos.right = node
        self.length += 1
        return self

    def pop(self):
        l = self.length
        if not l:
            raise IndexError("pop from empty tree")
        elif l == 1:
            rs, self.root = self.root, None
            self.length -= 1
            return rs
        path = bin(l)[3:-1]
        final = bin(l)[-1]
        pos = self.root
        rs = None
        # Travel to destination
        for i in path:
            pos = pos.left if i == '0' else pos.right
        # Get result and set tail to None
        if final == '0':
            rs, pos.left = pos.left, None
        else:
            rs, pos.right = pos.right, None
        self.length -= 1
        return rs

    def preorder(self, node, func):
        func(node)
        if node.left:
            self.preorder(node.left, func)
        if node.right:
            self.preorder(node.right, func)

    def inorder(self, node, func):
        if node.left:
            self.inorder(node.left, func)
        func(node)
        if node.right:
            self.inorder(node.right, func)

    def postorder(self, node, func):
        if node.left:
            self.inorder(node.left, func)
        if node.right:
            self.inorder(node.right, func)
        func(node)

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        return self.length
