from linked_list import LinkedList


class DivHashTable:
    def __init__(self, m):
        self.m = m
        self.T = []
        for i in range(0, m):
            self.T.append(LinkedList())

    def div_hash_function(self, key):
        return key % self.m

    def div_hash_insert(self, key):
        pos = self.div_hash_function(key)
        self.T[pos].add(key)

    def div_hash_remove(self, key):
        pos = self.div_hash_function(key)
        return self.T[pos].remove(key)

    def div_hash_search(self, key):
        pos = self.div_hash_function(key)
        return self.T[pos].search(key)
