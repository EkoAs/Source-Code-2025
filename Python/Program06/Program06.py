import math 
import random

data_int = 29
data_float = 29.0
data_bool = True
data_str = "29"

# matrix in python
# Create a 2D list (matrix) with 3 rows and 4 columns # with random a number 
# between 1 and 100
matrix = [[random.randint(1, 2) for _ in range(4)] for _ in range(3)]
print("Matrix:")
for row in matrix:
    print(row) 

# create password a generator with python simple
# import random 
import random
input("Enter the length of the password: ")
length = int(input("Enter the length of the password: "))
password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length)) 
print("Generated password:", password)

