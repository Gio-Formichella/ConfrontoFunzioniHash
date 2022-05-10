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

# results list threw all tests
div_table_results = []
mul_table_results = []

for test in range(0, n_tests):
    div_tables = []  # list of DivHashTables
    mul_tables = []  # list of MulHashTables
    keys = []  # keeps track inserted keys

    div_tables_performance = []
    mul_tables_performance = []

    for dim in dimensions:
        div_tables.append(DivHashTable(dim))
        mul_tables.append(MulHashTable(dim))
        # dictionaries will hold test results: { load factor : [exec_time , collision number] }
        div_result_dict = {}
        mul_result_dict = {}
        div_tables_performance.append(div_result_dict)
        mul_tables_performance.append(mul_result_dict)

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
                div_tables_performance[i][a] = [end - start,
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
                mul_tables_performance[i][a] = [end - start,
                                                collisions]  # adding result to correct dictionary from list

                ongoing = True

    # adding performance to performances list
    div_table_results.append(div_tables_performance)
    mul_table_results.append(mul_tables_performance)

    for i in range(0, len(div_tables_performance)):
        pickle.dump(keys, open("results/insertion/test" + str(test + 1) + "_keys.p"))
        pickle.dump(div_tables_performance[i], open(
            "results/insertion/test" + str(test + 1) + "_DivHashTable_insertion_m=" + str(dimensions[i]) + "_results.p",
            "wb"))
        pickle.dump(mul_tables_performance[i], open(
            "results/insertion/test" + str(test + 1) + "_MulHashTable_insertion_m=" + str(dimensions[i]) + "_results.p",
            "wb"))

# average insertion run time
div_ins_time_sum = 0
div_ins_number = 0
mul_ins_time_sum = 0
mul_ins_number = 0

for i in range(0, n_tests):
    for j in range(0, len(div_table_results[i])):
        div_ins_time_sum += div_table_results[i][j][1][0]  # accessing exec_time, results[test[table[list[exec_time]]]]
        div_ins_number += 1
    for j in range(0, len(mul_table_results[i])):
        mul_ins_time_sum += mul_table_results[i][j][1][0]  # accessing exec_time, results[test[table[list[exec_time]]]]
        mul_ins_number += 1

time_result = {
    "DivHashTable": div_ins_time_sum / div_ins_number * 1000000,  # value in micro seconds
    "MulHashTable": mul_ins_time_sum / mul_ins_number * 1000000  # value in micro seconds
}
pickle.dump(time_result, open("average_insertion_time.p", "wb"))
