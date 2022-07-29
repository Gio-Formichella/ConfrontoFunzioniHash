from timeit import default_timer as timer
import numpy as np
from div_hash_table import *
from mul_hash_table import *
import pickle

dimensions = [2048, 2053]
div_function_time = 0
mul_function_time = 0

for dim in dimensions:
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
result = {"DivHashFunction": div_function_time * (10 ** 6) / (len(dimensions) * 100),
          "MulHashFunction": mul_function_time * (10 ** 6) / (len(dimensions) * 100)}

pickle.dump(result, open("results/hash_function/hash_function_result.p", "wb"))
