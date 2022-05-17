import pickle
import matplotlib.pyplot as plt

import insertion_test
import search_test
import remove_test
# running tests
test1 = insertion_test
test2 = search_test
test3 = remove_test
exec("test1")
exec("test2")
exec("test3")

# plotting insertion results
ins_time = pickle.load(open("results/insertion/averaged_insertion_time.p", "rb"))
x = list(ins_time.keys())
y = list(ins_time.values())
plt.figure()
plt.bar(x, y, color='C1', width=0.5)
plt.ylabel("$\mu$s")

# 13 cell tables
first_div_coll = pickle.load(open("results/insertion/div_averaged_collisions_m=13.p", "rb"))
first_mul_coll = pickle.load(open("results/insertion/mul_averaged_collisions_m=13.p", "rb"))
x1 = list(first_div_coll.keys())
y1 = list(first_div_coll.values())
x2 = list(first_mul_coll.keys())
y2 = list(first_mul_coll.values())
plt.figure()
plt.plot(x1, y1, 'r', label='DivHashTable')
plt.plot(x2, y2, 'b', label='MulHashTable')
plt.legend()
plt.xlabel("load factor")

# 16 cell tables
second_div_coll = pickle.load(open("results/insertion/div_averaged_collisions_m=16.p", "rb"))
second_mul_coll = pickle.load(open("results/insertion/mul_averaged_collisions_m=16.p", "rb"))
x3 = list(second_div_coll.keys())
y3 = list(second_div_coll.values())
x4 = list(second_mul_coll.keys())
y4 = list(second_mul_coll.values())
plt.figure()
plt.plot(x3, y3, 'g', label='DivHashTable')
plt.plot(x4, y4, 'm', label='MulHashTable')
plt.legend()
plt.xlabel("load factor")

plt.show()

# printing search and remove results
for i in [0.5, 1, 2]:
    div_suc_search_file = pickle.load(open("results/search/div_suc_results_ld="+str(i)+".p", "rb"))
    mul_suc_search_file = pickle.load(open("results/search/mul_suc_results_ld="+str(i)+".p", "rb"))
    div_unsuc_search_file = pickle.load(open("results/search/div_unsuc_results_ld="+str(i)+".p", "rb"))
    mul_unsuc_search_file = pickle.load(open("results/search/mul_unsuc_results_ld="+str(i)+".p", "rb"))
    div_remove_file = pickle.load(open("results/removal/div_remove_results_ld="+str(i)+".p", "rb"))
    mul_remove_file = pickle.load(open("results/removal/mul_remove_results_ld="+str(i)+".p", "rb"))

    print("DivHashTable successful search with load factor equal to " + str(i) + ":")
    for j in range(0, 5):
        print("test"+str(j+1)+": " + str(div_suc_search_file[j]*1000000))

    print("MulHashTable successful search with load factor equal to " + str(i) + ":")
    for j in range(0, 5):
        print("test"+str(j+1)+": " + str(mul_suc_search_file[j]*1000000))

    print("DivHashTable unsuccessful search with load factor equal to " + str(i) + ":")
    for j in range(0, 5):
        print("test"+str(j+1)+": " + str(div_unsuc_search_file[j]*1000000))
        
    print("MulHashTable unsuccessful search with load factor equal to " + str(i) + ":")
    for j in range(0, 5):
        print("test"+str(j+1)+": " + str(mul_unsuc_search_file[j]*1000000))

    print("DivHashTable removal with load factor equal to " + str(i) + ":")
    for j in range(0, 5):
        print("test"+str(j+1)+": " + str(div_remove_file[j]*1000000))

    print("MulHashTable removal with load factor equal to " + str(i) + ":")
    for j in range(0, 5):
        print("test"+str(j+1)+": " + str(mul_remove_file[j]*1000000))
