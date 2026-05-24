# take input from user with an auto detect data type bool or otherwise

# data = bool(int(input("Enter a number (0 or 1): "))) # 0 = False, 1 = True
# print("data_1:", data, "tipe data :", type(data))
# data_2 = input("masukan angka :")
# print("kamu memilih :", data_2)

#how to auto detect type data class. don't use '#' with input user

def auto_cast(value):
    try:
        # Try to convert to int
        int_val = int(value)
        if '.' not in value:
            return int_val
    except ValueError:
        pass
    try:
        # Try to convert to float
        float_val = float(value)
        return float_val
    except ValueError:
        pass
    if value.lower() in ['true', 'false']:
        # Convert to boolean
        return value.lower() == 'true'
    return value  # Return as string if no conversion is possible

user_input =input("Masukan sesuatu :")
typed_input = auto_cast(user_input)
print("Nilai:", {typed_input}, "tipe data:", {type(typed_input)})