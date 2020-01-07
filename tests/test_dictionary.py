import unittest
from data_structure_sample.data_structures.dictionary import Dictionary


class DictionaryTest(unittest.TestCase):

    def test_1(self):
        D1 = {}
        D_test = Dictionary()
        for i in [D1, D_test]:
            i[1] = ['one']
            i[2] = ['two']
            i[3] = ['three']
            i['array'] = [1, 2]
            i['s'] = ['string']
        self.assertEqual(D1[1], D_test[1])
        self.assertEqual(D1[2], D_test[2])
        self.assertEqual(D1[3], D_test[3])
        self.assertEqual(D1['array'], D_test['array'])
        self.assertEqual(D1['s'], D_test['s'])

    def test_2(self):
        D1 = {}
        D_test = Dictionary()
        n = 10000
        for j in range(n):
            D1[j] = D_test[j] = j*j
            D1[str(j)] = D_test[str(j)] = bin(j)
        for j in range(n):
            self.assertEqual(D1[j], D_test[j])
            self.assertEqual(D1[str(j)], D_test[str(j)])
