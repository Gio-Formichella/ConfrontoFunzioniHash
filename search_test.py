import pickle

import numpy as np
from timeit import default_timer as timer
from div_hash_table import *
from mul_hash_table import *

n_tests = 5
m = 13
a_factor = [0.5, 1, 2]  # load factors
u_min = 0
u_max = 99

div_table = DivHashTable(m)
mul_table = MulHashTable(m)
keys = []  # stores inserted keys

for ld in a_factor:
    div_suc_results = []
    mul_suc_results = []
    div_unsuc_results = []
    mul_unsuc_results = []
    searched_keys = []
    while div_table.get_load_factor() < ld:  # inserting up to load factor
        key = np.random.randint(u_min, u_max+1)
        keys.append(key)
        div_table.div_hash_insert(key)
        mul_table.mul_hash_insert(key)

    for i in range(0, n_tests):
        present_key = keys[np.random.randint(0, len(keys))]  # taking random key from keys
        absent_key = u_max + 1 + i  # key out of universe's range

        # successful search
        start = timer()
        div_table.div_hash_search(present_key)
        end = timer()
        div_suc_results.append(end - start)

        start = timer()
        mul_table.mul_hash_search(present_key)
        end = timer()
        mul_suc_results.append(end - start)

        # unsuccessful search
        start = timer()
        div_table.div_hash_search(absent_key)
        end = timer()
        div_unsuc_results.append(end - start)

        start = timer()
        mul_table.mul_hash_search(absent_key)
        end = timer()
        mul_unsuc_results.append(end - start)

        searched_keys.append(present_key)
        searched_keys.append(absent_key)

    pickle.dump(searched_keys, open("results/search/searched_keys_ld="+str(ld)+".p", "wb"))
