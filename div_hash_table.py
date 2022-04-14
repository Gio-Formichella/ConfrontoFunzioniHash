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
        pass

    def div_hash_remove(self, key):
        pass

    def div_hash_search(self, key):
        pass
