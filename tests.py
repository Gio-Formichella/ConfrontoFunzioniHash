from timeit import default_timer as timer
import numpy as np
from div_hash_table import *
from mul_hash_table import *
import pickle

table_dim = [2048, 2053]


def hash_function_test():  # testing average hash function execution time
    div_function_time = 0
    mul_function_time = 0

    for dim in table_dim:
        div_table = DivHashTable(dim)
        mul_table = MulHashTable(dim)
        for i in range(0, 100):
            key = np.random.randint(0, 9999)

            start = timer()
            div_table.div_hash_function(key)
            end = timer()
            div_function_time += end - start

            start = timer()
            mul_table.mul_hash_function(key)
            end = timer()
            mul_function_time += end - start

    # storing average hash function execution time in micro seconds
    result = {"DivHashFunction": div_function_time * (10 ** 6) / (len(table_dim) * 100),
              "MulHashFunction": mul_function_time * (10 ** 6) / (len(table_dim) * 100)}

    pickle.dump(result, open("results/hash_function/hash_function_result.p", "wb"))


def insertion_test():
    for dim in table_dim:
        keys = np.random.randint(0, 9999, dim * 2)  # U = [0,9999], max load factor = 2

        mul_table = MulHashTable(dim)
        div_table = DivHashTable(dim)

        # storing number of collisions every 50 insertions
        mul_collisions = {}
        div_collisions = {}
        mul_col_holder = 0
        div_col_holder = 0
        for i in range(0, len(keys)):
            key = keys[i]
            mul_col_holder += mul_table.mul_hash_insert(key)
            div_col_holder += div_table.div_hash_insert(key)

            if (i + 1) % 50 == 0:
                mul_collisions[i + 1] = mul_col_holder
                div_collisions[i + 1] = div_col_holder
                mul_col_holder = 0
                div_col_holder = 0

        pickle.dump(keys, open("results/insertion/keys_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(mul_collisions, open("results/insertion/mul_collisions_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(div_collisions, open("results/insertion/div_collisions_dim=" + str(dim) + ".p", "wb"))


def search_test():
    for dim in table_dim:
        keys = np.random.randint(0, 9999, dim * 2)  # U = [0,9999], max load factor = 2

        mul_table = MulHashTable(dim)
        div_table = DivHashTable(dim)

        # stores average number of inspected items for different table sizes
        mul_inspected = {}
        div_inspected = {}
        for i in range(0, len(keys)):
            key = keys[i]
            mul_table.mul_hash_insert(key)
            div_table.div_hash_insert(key)

            if (i + 1) % 50 == 0:  # counting average number of items inspected by search() every 50 new insertions
                mul_counter = 0
                div_counter = 0
                for j in range(0, i + 1):
                    mul_counter += mul_table.mul_hash_search(keys[j])[1]  # returns number of inspected items
                    div_counter += div_table.div_hash_search(keys[j])[1]  # returns number of inspected items
                mul_inspected[i + 1] = mul_counter / (i + 1)
                div_inspected[i + 1] = div_counter / (i + 1)

        pickle.dump(keys, open("results/search/keys_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(mul_inspected, open("results/search/mul_inspected_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(div_inspected, open("results/search/div_inspected_dim=" + str(dim) + ".p", "wb"))
