from timeit import default_timer as timer
import numpy as np
from div_hash_table import *
from mul_hash_table import *
import pickle


def hash_function_test(table_dim):  # testing average hash function execution time
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


def insertion_test(table_dim):
    for dim in table_dim:
        keys = np.random.randint(0, 9999, dim * 4)  # U = [0,9999], max load factor = 4

        mul_table = MulHashTable(dim)
        div_table = DivHashTable(dim)

        # storing number of collisions every 50 insertions
        mul_collisions = {}
        div_collisions = {}
        mul_col_counter = 0
        div_col_counter = 0
        for i in range(0, len(keys)):
            if mul_table.mul_hash_insert(keys[i]):  # if there was a collision
                mul_col_counter += 1
            if div_table.div_hash_insert(keys[i]):  # if there was a collision
                div_col_counter += 1
            # calculating average number of collisions every 50 insertions
            if (i + 1) % 50 == 0:
                mul_collisions[i + 1] = mul_col_counter / 50
                div_collisions[i + 1] = div_col_counter / 50
                mul_col_counter = 0
                div_col_counter = 0

        pickle.dump(keys, open("results/insertion/keys_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(mul_collisions, open("results/insertion/mul_collisions_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(div_collisions, open("results/insertion/div_collisions_dim=" + str(dim) + ".p", "wb"))


def search_test(table_dim):
    for dim in table_dim:
        keys = np.random.randint(0, 9999, dim * 2)  # U = [0,9999], max load factor = 2

        mul_table = MulHashTable(dim)
        div_table = DivHashTable(dim)

        # stores average number of inspected items for different table sizes
        mul_inspected = {}
        div_inspected = {}
        for i in range(0, len(keys)):
            mul_table.mul_hash_insert(keys[i])
            div_table.div_hash_insert(keys[i])

            if i % 50 == 0:
                # calculating average number of items inspected searching every key in tables
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


def remove_test(table_dim):
    for dim in table_dim:
        keys = np.random.randint(0, 9999, dim * 2)  # U = [0,9999], max load factor = 2

        mul_inspected = {}
        div_inspected = {}
        mul_table = MulHashTable(dim)
        div_table = DivHashTable(dim)
        for i in range(0, len(keys), 50):  # testing removal every 50 new insertions
            for j in range(0, i + 1):
                mul_table.mul_hash_insert(keys[j])
                div_table.div_hash_insert(keys[j])

            mul_counter = 0
            div_counter = 0
            for j in range(0, i + 1):
                mul_counter += mul_table.mul_hash_remove(keys[j])[1]  # returns inspected items
                div_counter += div_table.div_hash_remove(keys[j])[1]  # returns inspected items
            # storing average number of inspected elements to remove i keys
            mul_inspected[i] = mul_counter / (i + 1)
            div_inspected[i] = div_counter / (i + 1)
        pickle.dump(keys, open("results/removal/keys_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(mul_inspected, open("results/removal/mul_inspected_dim=" + str(dim) + ".p", "wb"))
        pickle.dump(div_inspected, open("results/removal/div_inspected_dim=" + str(dim) + ".p", "wb"))
