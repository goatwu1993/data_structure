

def max_heapify(heap):
    def swap(heap, i):
        l = len(heap)
        if 2*i + 2 > l:
            return
        if heap[2*i+1] > heap[i]:
            heap[2*i+1], heap[i] = heap[i], heap[2*i+1]
        if ((2*i+2 < l)
                and heap[2*i+2] > heap[i]):
            heap[2*i+2], heap[i] = heap[i], heap[2*i+2]
    l = len(heap)
    for i in reversed(range(l//2)):
        swap(heap, i)


def min_heapify(heap):
    def swap(heap, i):
        l = len(heap)
        if 2*i + 2 > l:
            return
        if heap[2*i+1] < heap[i]:
            heap[2*i+1], heap[i] = heap[i], heap[2*i+1]
        if ((2*i+2 < l)
                and heap[2*i+2] < heap[i]):
            heap[2*i+2], heap[i] = heap[i], heap[2*i+2]
    l = len(heap)
    for i in reversed(range(l//2)):
        swap(heap, i)


def ismaxheap(heap):
    def checkmaxheap(heap, i):
        l = len(heap)
        if 2*i + 2 > l:
            return True
        if heap[2*i+1] > heap[i]:
            return False
        if ((2*i+2 < l)
                and heap[2*i+2] > heap[i]):
            return False
        return True
    l = len(heap)
    for i in reversed(range(l//2)):
        checkmaxheap(heap, i)


def isminheap(heap):
    def checkminheap(heap, i):
        l = len(heap)
        if 2*i + 2 > l:
            return
        if heap[2*i+1] < heap[i]:
            heap[2*i+1], heap[i] = heap[i], heap[2*i+1]
        if ((2*i+2 < l)
                and heap[2*i+2] < heap[i]):
            heap[2*i+2], heap[i] = heap[i], heap[2*i+2]
    l = len(heap)
    for i in reversed(range(l//2)):
        swap(heap, i)
