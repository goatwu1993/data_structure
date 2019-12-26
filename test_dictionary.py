import unittest
from dictionary import Dictionary


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

    # def test_useful(self):
    #   self.assertDictEqual(self.D1, self.D2)
