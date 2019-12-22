class CompleteBinaryTreeNode():
    def __init__(self):
        self.left = None
        self.right = None


class CompleteBinaryTree():
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self):
        if not self.length:
            self.root = CompleteBinaryTreeNode()
            self.length += 1
        path = bin(self.length + 1)[3:-1]
        final = bin(self.length + 1)[-1]
        pos = self.root
        for i in path:
            pos = pos.left if i == '0' else pos.right
        if final == '0':
            pos.left = CompleteBinaryTreeNode()
        else:
            pos.right = CompleteBinaryTreeNode()
        self.length += 1
        return

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        return self.length
