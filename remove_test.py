from div_hash_table import *
from mul_hash_table import *
import pickle
import numpy as np
from timeit import default_timer as timer

n_tests = 5
m = 13
a_factor = [0.5, 1, 2]  # load factors
u_min = 0
u_max = 99

div_table = DivHashTable(m)
mul_table = MulHashTable(m)
keys = []  # stores inserted keys

for ld in a_factor:
    div_remove_results = []
    mul_remove_results = []
    deleted_keys = []
    while div_table.get_load_factor() < ld:  # inserting up to load factor
        key = np.random.randint(u_min, u_max + 1)
        keys.append(key)
        div_table.div_hash_insert(key)
        mul_table.mul_hash_insert(key)

    for i in range(0, n_tests):
        deleted_key = keys[np.random.randint(0, len(keys))]  # choosing key randomly
        deleted_keys.append(deleted_key)

        # testing remove method
        start = timer()
        div_table.div_hash_remove(deleted_key)
        end = timer()
        div_remove_results.append(end - start)

        start = timer()
        mul_table.mul_hash_remove(deleted_key)
        end = timer()
        mul_remove_results.append(end - start)

        # restoring load factor
        key = np.random.randint(u_min, u_max + 1)
        keys.append(key)
        div_table.div_hash_insert(key)
        mul_table.mul_hash_insert(key)

    pickle.dump(div_remove_results, open("results/removal/div_remove_results_ld=" + str(ld) + ".p", "wb"))
    pickle.dump(mul_remove_results, open("results/removal/mul_remove_results_ld=" + str(ld) + ".p", "wb"))
    pickle.dump(deleted_keys, open("results/removal/deleted_keys_ld=" + str(ld) + ".p", "wb"))

pickle.dump(keys, open("results/removal/keys.p", "wb"))
