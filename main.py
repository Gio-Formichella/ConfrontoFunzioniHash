import pickle
import matplotlib.pyplot as plt
import tests

# exec("tests.hash_function_test()")
# exec("tests.insertion_test()")
# exec("tests.search_test()")

# hash_function_test plot
result = pickle.load(open("results/hash_function/hash_function_result.p", "rb"))
x = list(result.keys())
y = list(result.values())
plt.figure()
plt.bar(x[0], y[0], color='r')
plt.bar(x[1], y[1], color='orange')
plt.ylabel("$\mu$s")

# insertion plot
div_collisions = pickle.load(open("results/insertion/div_collisions_dim=2048.p", "rb"))
mul_collisions = pickle.load(open("results/insertion/mul_collisions_dim=2048.p", "rb"))
x1 = list(div_collisions.keys())
y1 = list(div_collisions.values())
x2 = list(mul_collisions.keys())
y2 = list(mul_collisions.values())
plt.figure()
plt.plot(x1, y1, 'r', label="DivHashTable")
plt.plot(x2, y2, 'orange', label="MulHashTable")
plt.ylabel("collisions")

div_collisions = pickle.load(open("results/insertion/div_collisions_dim=2053.p", "rb"))
mul_collisions = pickle.load(open("results/insertion/mul_collisions_dim=2053.p", "rb"))
x1 = list(div_collisions.keys())
y1 = list(div_collisions.values())
x2 = list(mul_collisions.keys())
y2 = list(mul_collisions.values())
plt.figure()
plt.plot(x1, y1, 'r', label="DivHashTable")
plt.plot(x2, y2, 'orange', label="MulHashTable")
plt.ylabel("collisions")

# search plot
div_inspected = pickle.load(open("results/search/div_inspected_dim=2048.p", "rb"))
mul_inspected = pickle.load(open("results/search/mul_inspected_dim=2048.p", "rb"))
x1 = list(div_inspected.keys())
y1 = list(div_inspected.values())
x2 = list(mul_inspected.keys())
y2 = list(mul_inspected.values())
plt.figure()
plt.plot(x1, y1, 'r', label="DivHashTable")
plt.plot(x2, y2, 'orange', label="MulHashTable")

div_inspected = pickle.load(open("results/search/div_inspected_dim=2053.p", "rb"))
mul_inspected = pickle.load(open("results/search/mul_inspected_dim=2053.p", "rb"))
x1 = list(div_inspected.keys())
y1 = list(div_inspected.values())
x2 = list(mul_inspected.keys())
y2 = list(mul_inspected.values())
plt.figure()
plt.plot(x1, y1, 'r', label="DivHashTable")
plt.plot(x2, y2, 'orange', label="MulHashTable")

plt.show()
