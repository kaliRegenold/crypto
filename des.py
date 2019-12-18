
DES_s1 = [[0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000],
          [0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011]]

DES_s2 = [[0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010],
          [0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100]]

def swap_bits(b):
    return ((b << 6) | ((b & (0b111111<<6)) >> 6)) & ((2**12)-1)

def DES_get_round_key(key, i):
    return (((key << 9) | key) & ((2**8-1) << (9-i+2))) >> (9-i+2)

def DES_f(block, key_i):
    # Expander function
    # 123456 -> 12434356
    exp_1 = ((block & 0b110000) >> 2) | \
            ((block & 0b000100) >> 1) | \
            ((block & 0b001000) >> 3)
    exp_2 = ((exp_1 & 0b000011) << 2) | \
            ((block & 0b000011))

    exp_1 ^= ((key_i & 0b11110000) >> 4)
    exp_2 ^= ((key_i & 0b00001111))

    # S-Block look up
    # Bit 1 is row; bits 2, 3, 4 are column
    s1_output = DES_s1 [(exp_1 & 0b1000) >> 3] [(exp_1 & 0b0111)]
    s2_output = DES_s2 [(exp_2 & 0b1000) >> 3] [(exp_2 & 0b0111)]

    # Combine S-Block outputs
    return s1_output << 4 | s2_output


def DES_encrypt(block, key, num_rounds=4):
    for i in range(1, num_rounds+1):
        block_l = (block & 0b111111000000) >> 6
        block_r = (block & 0b000000111111)
        temp_l = block_r
        block_r = block_l ^ (DES_f(block_r, DES_get_round_key(key, i)))
        block_l = temp_l
    return (block_l << 6) | (block_r)

def DES_decrypt(block, key, num_rounds=4):
    # Reverse the key
    rev_key = 0
    for i in range(0,9):
        if key & (1 << i):
            rev_key |= 1 << (8-i)
    # Swap left and right parts of block
    block = swap_bits(block)
    dec =  DES_encrypt(block, key, num_rounds)
    return swap_bits(dec)


if __name__ == "__main__":
    r = 0b011100100110
    k = 0b011001010
    enc = DES_encrypt(r, k, 1)
    dec = DES_decrypt(enc, k, 1)
    print("r:   {0:012b}".format(r))
    print("enc: {0:012b}".format(enc))
    print("dec: {0:012b}".format(dec))
