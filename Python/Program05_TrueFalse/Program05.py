print("=========True==========")
data_bool = True
print(data_bool + 1) # Output: 2 # True is treated as 1 in arithmetic operations
print(data_bool + 0) # Output: 1 # True is treated as 1 in arithmetic operations 

print("===========False=============")
data_bool2 = False
print(data_bool2 + 1) # Output: 1 # False is treated as 0 in arithmetic operations  
print(data_bool2 + 0) # Output: 0 # False is treated as 0 in arithmetic operations

import math
import random
n = 85
r = 20
r_1 = 35
n_2 = 53
n_1 = n - r_1
def kombinasi(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
peluang = kombinasi(n_2,r_1)/ kombinasi(n,r)
print("Peluangnya", {peluang})
data_int = int(peluang), 
data_float = float(peluang), 
data_bool = bool(peluang)
print("jadi hasilnya adalah", data_int, "Type =", type(data_int))  # Output: 0 <class 'int'>
print("jadi hasilnya adalah", data_float, "Type =", type(data_float))  # Output: 0.0 <class 'float'>
print("jadi hasilnya adalah", data_bool, "Type =", type(data_bool))  # Output: 0 <class 'bool'>