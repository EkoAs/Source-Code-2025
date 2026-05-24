# Program04.py
print("==========INTEGER==========")
#DATA INTEGER
data_1 = 9 # Convert integer to string
data_str = str(data_1)  # Convert integer to stringprint(data_str, type(data_str))  # Output: '9' <class 'str'>
# Convert integer to float
data_float = float(data_1) 
data_str = str(data_1)
data_bool = bool(data_1)  # Convert integer to boolean #akan false jika nilai int 0 

# Convert integer to float
print("data =", data_float, "Type =", type(data_float))  # Output: 9.0
print("data =", data_str, "Type =", type(data_str))  # Output: '9' <class 'str'>
print("data =", data_bool, "Type =", type(data_bool))  # Output: True <class 'bool'>



#DATA FLOAT
print("===========FLOAT=============")

data_float = 9
# Convert float to string
print("data =", data_float, "Type =", type(data_float))  # Output: 9.0 <class 'float'>

data_str = str(data_float)  # Convert float to string
print("data =", data_str, "Type =", type(data_str))  # Output: '9.0' <class 'str'>

data_int = int(data_float)  # Convert float to integer #akan dibulatkan ke bawah
print("data =", data_int, "Type =", type(data_int))  # Output: 9 <class 'int'>

data_bool = bool(data_float)  # Convert float to boolean #akan false jika nilai float 0.0
print("data =", data_bool,"Type =", type(data_bool))  # Output: True <class 'bool'>


#DATA BOOLEAN
print("===========BOOLEAN=============")
data_bool = True # Convert boolean to string
data_str = str(data_bool)  # Convert boolean to string
print("data =", data_str, "Type =", type(data_str))  # Output: 'True' <class 'str'>

# Convert boolean to integer
data_int = int(data_bool)  # Convert boolean to integer #akan false jika nilai boolean False
print("data =", data_int, "Type =", type(data_int))  # Output: 1 <class 'int'>

# Convert boolean to float
data_float = float(data_bool)  # Convert boolean to float #akan false jika nilai boolean False
print("data =", data_float, "Type =", type(data_float))  # Output: 1.0 <class 'float'>

# Convert boolean to string
data_str = str(data_bool)  # Convert boolean to string
print("data =", data_str, "Type =", type(data_str))  # Output: 'True' <class 'str'>

#DATA STRING
print("===========STRING=============")
data_str = "9"  # Convert string to integer #string harus angka dan akan fale jika kosong
print("data =", data_str, "Type =", type(data_str))  # Output: '9' <class 'str'>

# Convert string to integer
data_int = int(data_str)  # Convert string to integer
print("data =", data_int, "Type =", type(data_int))  # Output: 9 <class 'int'>

# Convert string to float
data_float = float(data_str)  # Convert string to float
print("data =", data_float, "Type =", type(data_float))  # Output: 9.0 <class 'float'>

# Convert string to boolean
data_bool = bool(data_str)
print("data =", data_bool, "Type =", type(data_bool)) 

# Output: True <class 'bool'>
# Convert string to boolean (empty string "")




















