import numpy as np

import insertion_test
import search_test
import remove_test
import pickle
import matplotlib.pyplot as plt

test1 = insertion_test
test2 = search_test
test3 = remove_test
exec("test1")
exec("test2")
exec("test3")

ins_time = pickle.load(open("results/insertion/averaged_insertion_time.p", "rb"))
x = list(ins_time.keys())
y = list(ins_time.values())
plt.bar(x, y, color='C1', width=0.5)
plt.ylabel("$\mu$s")
plt.show()
