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
        self.assertEqual(self.table.div_hash_function(4), 4 % self.table.m)
        self.assertEqual(self.table.div_hash_function(13), 13 % self.table.m)
        self.assertEqual(self.table.div_hash_function(24), 24 % self.table.m)

    def test_div_hash_insert(self):
        key = 7
        self.table.div_hash_insert(7)

        self.assertTrue(self.table.T[self.table.div_hash_function(key)].search(key))

        key2 = 12
        self.table.div_hash_insert(key2)
        self.table.div_hash_insert(key2)

        self.assertTrue(self.table.T[self.table.div_hash_function(key2)].search(key2))
        self.assertTrue(self.table.T[self.table.div_hash_function(key2)].search(key2))
