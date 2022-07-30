import unittest
from div_hash_table import DivHashTable


class TestDivHashTable(unittest.TestCase):

    def test_init(self):
        m = 10
        table = DivHashTable(m)

        self.assertEqual(table.m, m)
        for i in range(0, m):
            self.assertTrue(table.T[i].is_empty())

    def setUp(self):
        self.table = DivHashTable(13)

    def test_div_hash_function(self):
        key1 = 4
        key2 = 13
        key3 = 24
        self.assertEqual(self.table.div_hash_function(key1), key1 % self.table.m)
        self.assertEqual(self.table.div_hash_function(key2), key2 % self.table.m)
        self.assertEqual(self.table.div_hash_function(key3), key3 % self.table.m)

    def test_div_hash_insert(self):
        key = 7
        col = self.table.div_hash_insert(key)

        self.assertFalse(col)
        self.assertTrue(self.table.T[self.table.div_hash_function(key)].search(key))

        key2 = 12
        key3 = 12 + self.table.m
        self.table.div_hash_insert(key2)

        col = self.table.div_hash_insert(key3)
        self.assertTrue(col)

        self.assertTrue(self.table.T[self.table.div_hash_function(key2)].search(key2))
        self.assertTrue(self.table.T[self.table.div_hash_function(key3)].search(key3))

    def test_div_hash_remove(self):
        key = 7
        self.table.div_hash_insert(key)

        key2 = 12
        self.table.div_hash_insert(key2)
        self.table.div_hash_insert(key2)

        self.assertTrue(self.table.div_hash_remove(key)[0])
        self.assertTrue(self.table.div_hash_remove(key2)[0])
        self.assertFalse(self.table.div_hash_remove(0)[0])

    def test_div_hash_search(self):
        key1 = 5
        key2 = 5 + self.table.m
        key3 = 5 + self.table.m * 2

        self.table.div_hash_insert(key1)
        self.table.div_hash_insert(key2)
        self.table.div_hash_insert(key3)
        self.table.div_hash_insert(key1)
        self.table.div_hash_insert(key1)

        self.assertTrue(self.table.div_hash_search(key1)[0])
        self.assertEqual(self.table.div_hash_search(key3)[1], 3)
        self.assertTrue(self.table.div_hash_search(key2)[0])
        self.assertTrue(self.table.div_hash_search(key3)[0])

        self.table.div_hash_remove(key2)
        self.assertFalse(self.table.div_hash_search(key2)[0])
        self.assertFalse(self.table.div_hash_search(key1 + 1)[0])
