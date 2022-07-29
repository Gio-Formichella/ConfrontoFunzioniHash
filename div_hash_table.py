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
        return self.T[pos].size() - 1  # returns number of collisions

    def div_hash_remove(self, key):
        pos = self.div_hash_function(key)
        return self.T[pos].remove(key)

    def div_hash_search(self, key):
        pos = self.div_hash_function(key)
        return self.T[pos].search(key)

    def get_load_factor(self):
        n = 0
        for linkedlist in self.T:
            n += linkedlist.size()
        return n / self.m

    def get_collision_number(self):
        collisions = 0
        for linkedlist in self.T:
            size = linkedlist.size()
            if size > 1:
                collisions += size - 1

        return collisions
