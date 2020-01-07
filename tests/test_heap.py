import unittest
from data_structure_sample.data_structures.heap import Heap, HeapUtils
import heapq


class HeapTest(unittest.TestCase):

    def test_1(self):
        Heap_real = []
        Heap_test = Heap()
        for i in [Heap_real, Heap_test]:
            for j in range(10):
                i.append(j*j)
        for i in [Heap_real, Heap_test]:
            for j in range(10):
                i.append(j*j)
        for i in [Heap_real, Heap_test]:
            for j in range(10):
                i.append(j*j)
        hu = HeapUtils()
        heapq.heapify(Heap_real)
        self.assertTrue(hu.is_minheap(Heap_real))
        self.assertTrue(hu.is_minheap(Heap_test))

    def test_2(self):
        Heap_real = []
        Heap_test = Heap()
        n = 40
        for j in range(n):
            Heap_real.append(j)
            Heap_test.append(j)
        for j in range(n):
            Heap_real.append(j)
            Heap_test.append(j)
        hu = HeapUtils()
        heapq.heapify(Heap_real)
        self.assertTrue(hu.is_minheap(Heap_real))
        self.assertTrue(hu.is_minheap(Heap_test))
