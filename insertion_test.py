import numpy as np
import pickle
from div_hash_table import *
from mul_hash_table import *


def insertion_test():
    table_dim = [2048, 2053]
    max_load_factor = 1.4

    for dim in table_dim:
        keys = np.random.randint(0, 9999, int(dim * max_load_factor))  # U = [0,9999]

        mul_table = MulHashTable(dim)
        div_table = DivHashTable(dim)

        mul_collisions = {}
        div_collisions = {}
        for i in range(0, len(keys)):
            mul_table.mul_hash_insert(keys[i])
            div_table.div_hash_insert(keys[i])

            mul_collisions[i] = mul_table.get_collision_number()
            div_collisions[i] = div_table.get_collision_number()

        pickle.dump(keys, open("results/insertion/keys_dim="+str(dim)+".p", "wb"))
        pickle.dump(mul_collisions, open("results/insertion/mul_collisions_dim="+str(dim)+".p", "wb"))
        pickle.dump(div_collisions, open("results/insertion/div_collisions_dim="+str(dim)+".p", "wb"))
