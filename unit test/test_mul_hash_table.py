import unittest
from mul_hash_table import *


class TestMulHashTable(unittest.TestCase):

    def test_init(self):
        m = 10
        table = MulHashTable(m)

        self.assertEqual(table.m, m)
        for i in range(0, m):
            self.assertTrue(table.T[i].is_empty())

    def setUp(self):
        self.table = MulHashTable(13)
        self.a = (math.sqrt(5)-1)/2  # Knuth's suggested A value

    def test_mul_hash_funtion(self):
        key1 = 4
        key2 = 13
        key3 = 24
        self.assertEqual(self.table.mul_hash_function(key1), math.floor(self.table.m*((key1*self.a) % 1)))
        self.assertEqual(self.table.mul_hash_function(key2), math.floor(self.table.m*((key2*self.a) % 1)))
        self.assertEqual(self.table.mul_hash_function(key3), math.floor(self.table.m*((key3*self.a) % 1)))

    def test_mul_hash_insert(self):
        key = 7
        self.table.mul_hash_insert(key)

        self.assertTrue(self.table.T[self.table.mul_hash_function(key)].search(key))

        key2 = 12
        key3 = 12 + self.table.m
        self.table.mul_hash_insert(key2)
        self.table.mul_hash_insert(key3)

        self.assertTrue(self.table.T[self.table.mul_hash_function(key2)].search(key2))
        self.assertTrue(self.table.T[self.table.mul_hash_function(key3)].search(key3))

    def test_mul_hash_remove(self):
        key = 7
        self.table.mul_hash_insert(key)

        key2 = 12
        self.table.mul_hash_insert(key2)
        self.table.mul_hash_insert(key2)

        self.assertTrue(self.table.mul_hash_remove(key))
        self.assertTrue(self.table.mul_hash_remove(key2))
        self.assertFalse(self.table.mul_hash_remove(0))

    def test_div_hash_search(self):
        key1 = 5
        key2 = 5 + self.table.m
        key3 = 5 + self.table.m * 2

        self.table.mul_hash_insert(key1)
        self.table.mul_hash_insert(key2)
        self.table.mul_hash_insert(key3)
        self.table.mul_hash_insert(key1)
        self.table.mul_hash_insert(key1)

        self.assertTrue(self.table.mul_hash_search(key1))
        self.assertTrue(self.table.mul_hash_search(key2))
        self.assertTrue(self.table.mul_hash_search(key3))

        self.table.mul_hash_remove(key2)
        self.assertFalse(self.table.mul_hash_search(key2))
        self.assertFalse(self.table.mul_hash_search(key1+1))


if __name__ == '__main__':
    unittest.main()
