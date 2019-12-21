from linked_list.linked_list import LinkedList
from dictionary_openadressing.dictionary import Dictionary
from heap.heap import Heap
import operator

if __name__ == '__main__':
    h = Heap(compare=operator.gt)
    for i in range(0, 20, 1):
        h.insert(i)

    for i in range(0, 10, 1):
        h.insert(i)
