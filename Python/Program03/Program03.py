import random
import math
    #variabel tempat 



#tipe data
data_integer = 1
print("data :", data_integer, "bertipe", type(data_integer))

# data desimal, float
data_fload = 1.3
print("data : ", data_fload, "tipe", type(data_fload)) 

# data string, karakter
data_string = "hello"
print("data : ", data_string, "tipe", type(data_string)) 

# data biner, true/false boolean 
data_bool = True
print("data : ", data_bool, "tipe", type(data_bool)) 

#data khusus data kompleks
data_complex = complex(5,6)
print("data : ", data_complex, "tipe", type(data_complex)) 

#data bahasa c
from ctypes import c_double, c_char, c_int
data_c = c_double(10.4)
print("data : ", data_c, "tipe", type(data_c)) 