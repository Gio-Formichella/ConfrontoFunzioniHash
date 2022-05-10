import numpy as np
import pickle
from timeit import default_timer as timer
from div_hash_table import *
from mul_hash_table import *

n_tests = 5
dimensions = [13, 16]
# key universe range
u_min = 0
u_max = 99
a_max = 2  # max load factor

for test in range(0, n_tests):
    div_tables = []  # list of DivHashTables
    mul_tables = []  # list of MulHashTables
    keys = []  # keeps track inserted keys

    div_hash_table_results = []
    mul_hash_table_results = []

    for dim in dimensions:
        div_tables.append(DivHashTable(dim))
        mul_tables.append(MulHashTable(dim))
        # dictionaries will hold test results: { load factor : [exec_time , collision number] }
        div_hash_table_results.append(dict)
        mul_hash_table_results.append(dict)

    ongoing = True
    # testing insertion
    while ongoing:
        key = np.random.randint(u_min, u_max + 1)  # key from key universe
        keys.append(key)
        ongoing = False

        # testing DivHashTables
        for i in range(0, len(div_tables)):
            a = div_tables[i].get_load_factor()
            if a < a_max:  # insertion up to load factor
                start = timer()
                div_tables[i].div_hash_insert(key)
                end = timer()

                collisions = div_tables[i].get_collision_number()
                div_hash_table_results[i][a] = [end - start,
                                                collisions]  # adding result to correct dictionary from list

                ongoing = True

        # testing MulHashTable
        for i in range(0, len(mul_tables)):
            a = mul_tables[i].get_load_factor()
            if a < a_max:  # insertion up to load factor
                start = timer()
                mul_tables[i].mul_hash_insert(key)
                end = timer()

                collisions = mul_tables[i].get_collision_number()
                mul_hash_table_results[i][a] = [end - start,
                                                collisions]  # adding result to correct dictionary from list

                ongoing = True
