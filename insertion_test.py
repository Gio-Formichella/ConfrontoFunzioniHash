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

div_time = 0  # stores total insertion run time for div_hash_insert()
mul_time = 0  # stores total insertion run time for mul_hash_insert()
total_ins = 0  # total number of insertions, used for time average

for dim in dimensions:
    inserted_keys = math.floor(a_max * dim)  # number of input keys
    collision_div_counter = np.zeros(
        (inserted_keys, 1))  # collision_div_counter[i] = total number of collision up to i-th insertion
    collision_mul_counter = np.zeros(
        (inserted_keys, 1))  # collision_mul_counter[i] = total number of collision up to i-th insertion

    for test in range(0, n_tests):
        div_table = DivHashTable(dim)
        mul_table = MulHashTable(dim)

        keys = []
        div_test_result = []  # used for pickling test result
        mul_test_result = []  # used for pickling test result

        for i in range(0, inserted_keys):
            key = np.random.randint(u_min, u_max + 1)
            keys.append(key)

            # testing insertion on DivHashTable
            start = timer()
            div_table.div_hash_insert(key)
            end = timer()

            div_time += end - start
            collision_div_counter[i] += div_table.get_collision_number()
            div_test_result.append([end - start, div_table.get_collision_number()])

            # testing insertion on MulHashTable
            start = timer()
            mul_table.mul_hash_insert(key)
            end = timer()

            mul_time += end - start
            collision_mul_counter[i] += mul_table.get_collision_number()
            mul_test_result.append([end - start, mul_table.get_collision_number()])

        pickle.dump(keys, open("results/insertion/test" + str(test) + "_m=" + str(dim) + "_keys.p", "wb"))
        pickle.dump(div_test_result,
                    open("results/insertion/div_test" + str(test) + "_m=" + str(dim) + "_result.p", "wb"))
        pickle.dump(mul_test_result,
                    open("results/insertion/mul_test" + str(test) + "_m=" + str(dim) + "_result.p", "wb"))

    total_ins += inserted_keys * n_tests

    # average collision number
    averaged_div_lf_to_collision = {}  # {load factor : collisions}
    averaged_mul_lf_to_collision = {}  # {load factor : collisions}
    for i in range(0, inserted_keys):
        collision_div_counter[i] = collision_div_counter[i] / n_tests
        collision_mul_counter[i] = collision_mul_counter[i] / n_tests

        averaged_div_lf_to_collision[i / dim] = collision_div_counter[i]
        averaged_mul_lf_to_collision[i / dim] = collision_mul_counter[i]

    pickle.dump(averaged_div_lf_to_collision,
                open("results/insertion/div_averaged_collisions_m=" + str(dim) + ".p", "wb"))
    pickle.dump(averaged_mul_lf_to_collision,
                open("results/insertion/mul_averaged_collisions_m=" + str(dim) + ".p", "wb"))

exec_time = {
    "DivHashTable": div_time / total_ins * 1000000,  # average time in microseconds
    "MulHashTable": mul_time / total_ins * 1000000  # average time in microseconds
}
pickle.dump(exec_time, open("results/insertion/averaged_insertion_time.p", "wb"))
