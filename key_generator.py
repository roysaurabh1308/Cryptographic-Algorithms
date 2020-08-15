# Parity Drop (64 bit to 56 bit)
def parity_drop(block_64):
    par_table = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    bit_56 = ""
    for index in par_table:
        bit_56 += key_64[index - 1]
    return(bit_56)

# print(key_56)



# Dividing key into two halfes (28 bit each)
def divide_28(key_56):
    first_28 = key_56[:28]
    second_28 = key_56[28:]
    return(first_28, second_28)

# print(first_28, second_28)



# Left shift of 28 bit keys
# Check no. of shifts
def check_nof_shift(round_no):
    if(round_no in [1,2,9,16]):
        nof_shift = 1
    else:
        nof_shift = 2
    return(nof_shift)
# Left shift operation
def left_shift(key, nof_shift):
    shifted = ""
    shifted = key[nof_shift:28] + key[:nof_shift]
    return(shifted)
# a = left_shift(first_28, nof_shift)
# b = left_shift(second_28, nof_shift)
# print("after shifting\n ")
# print(a, " ",b)


#combine two 28-bits parts to one single 56-bit key
def combine(a, b):
    key_56_new = a + b
    return(key_56_new)


# Key compression
def key_compression(key_56):
    comp_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    compressed_key = ""
    for i in comp_table:
        compressed_key += key_56[i - 1]
    return(compressed_key)

# comp_key = key_compression(key_56_new)
# print("compressed key is", comp_key)
# print(len(comp_key))


# KEY GENERATOR


def key_generator_part(round_no, a, b):
    nof_shift = check_nof_shift(round_no)
    a = left_shift(a, nof_shift)
    b = left_shift(b, nof_shift)
    n = a + b
    comp = key_compression(n)
    round_keys.append(comp)
    return(a, b)

def key_generator():
    
    round_no = 1
    nof_shift = check_nof_shift(round_no)
    a = left_shift(first_28, nof_shift)
    b = left_shift(second_28, nof_shift)
    c = a + b
    d = key_compression(c)
    round_keys.append(d)  #1st round key is appended
    for round_no in range(2, 17):
        a, b = key_generator_part(round_no, a, b)



key_64 = "0001001100110100010101110111100110011011101111001101111111110001"
key_56 = parity_drop(key_64)
first_28, second_28 = divide_28(key_56)
round_keys = []
key_generator()
print(round_keys)
