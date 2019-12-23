#from .linked_list.linked_list import LinkedList
import operator
from heap import Heap
#from .dictionary_openadressing.dictionary import Dictionary
import sys


if __name__ == '__main__':
    h = Heap(compare=operator.gt)
    for i in range(0, 7, 1):
        h.insert(i)

    for i in range(0, 7, 1):
        print(h.pop())
        
