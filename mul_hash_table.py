from linked_list import LinkedList
import math


class MulHashTable:
    def __init__(self, m):
        self.m = m
        self.T = []
        for i in range(0, m):
            self.T.append(LinkedList())

    def mul_hash_function(self, key):
        a = (math.sqrt(5)-1)/2  # Knuth's suggested A value
        return math.floor(self.m*((key*a) % 1))  # ritorna parte intera inferiore

    def mul_hash_insert(self, key):
        pos = self.mul_hash_function(key)
        self.T[pos].add(key)

    def mul_hash_remove(self, key):
        pos = self.mul_hash_function(key)
        return self.T[pos].remove(key)

    def mul_hash_search(self, key):
        pos = self.mul_hash_function(key)
        return self.T[pos].search(key)
