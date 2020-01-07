class Queue():
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)
        return self

    def dequeue(self):
        return self.items.pop()

    def __repr__(self):
        return "Queue:("+self.items.__repr__()+")"
