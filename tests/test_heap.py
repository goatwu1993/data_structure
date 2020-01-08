import unittest
#from data_structure_sample.data_structures.heap import Heap, HeapUtils
#from data_structure_sample.data_structures import myheapq
#import heapq


# class HeapTest(unittest.TestCase):

#     def test_1(self):
#         Heap_real = [1, 2, 3]
#         self.assertTrue(not myheapq.ismaxheap(Heap_real))
#         self.assertTrue(myheapq.isminheap(Heap_real))

#     def test_2(self):
#         Heap_real = [3, 2, 1]
#         self.assertTrue(myheapq.ismaxheap(Heap_real))
#         self.assertTrue(not myheapq.isminheap(Heap_real))

#     def test_3(self):
#         Heap_test = [2, 3, 1]
#         self.assertTrue(not myheapq.ismaxheap(Heap_test))
#         self.assertTrue(not myheapq.isminheap(Heap_test))

#     def test_4(self):
#         Heap_real = [i for i in range(200)]
#         self.assertTrue(not myheapq.ismaxheap(Heap_real))
#         self.assertTrue(myheapq.isminheap(Heap_real))

#     def test_5(self):
#         Heap_real = [i for i in range(200, 0, -1)]
#         self.assertTrue(myheapq.ismaxheap(Heap_real))
#         self.assertTrue(not myheapq.isminheap(Heap_real))

#     def test_6(self):
#         Heap_test = [i for i in range(100, 200)] + \
#             [i for i in range(100, 0, -1)]
#         self.assertTrue(not myheapq.ismaxheap(Heap_test))
#         self.assertTrue(not myheapq.isminheap(Heap_test))

#     def test_7(self):
#         Heap_test = [i for i in range(10, 20)] + \
#             [i for i in range(10, 0, -1)]
#         self.assertTrue(not myheapq.ismaxheap(Heap_test))
#         self.assertTrue(not myheapq.isminheap(Heap_test))
#         myheapq.min_heapify(Heap_test)
#         print(Heap_test)
#         self.assertTrue(not myheapq.ismaxheap(Heap_test))
#         self.assertTrue(myheapq.isminheap(Heap_test))
