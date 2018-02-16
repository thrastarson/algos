def get_bit(num, i):
    #Return the value of the i-th bit in num.
    num = int(to_binary_string(num), 2)
    mask = 1 << i
    return 1 if num & mask else 0

def set_bit(num, i):
    #Sets the i-th bit in num to be 1.
    num = int(to_binary_string(num), 2)
    mask = 1 << i
    return num | mask

def clear_bit(num, i)
    num = int(to_binary_string(num), 2)
    mask = ~(1 << i)
    return num & mask

def update_bit(num, i, bit_is_1):
    num = int(to_binary_string(num), 2)
    cleared = clear_bit(num, i)
    bit = 1 if bit_is_1 else 0
    mask = ~(1 << i)
    return cleared | (bit_is_1 << i)

def print_binary(num):
    #Num is an int.
    print(to_binary_string(num))

def to_binary_string(num):
    return "{0:b}".format(num)

def main():
    num = 113
    print_binary(num)

    bit = get_bit(num, 3)
    print(bit)

    num = set_bit(num, 3)
    print_binary(num)

if __name__ == '__main__':
    main()
