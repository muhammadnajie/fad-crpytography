"""Simple keystream with 4 indeces gap"""

import re

def main():
    ldn_bit = ord("1")
    ldn_bin = bin(ldn_bit)
    ldn = re.sub("0b", "", ldn_bin)
    ldn_len = len(ldn)

    for i in range(2**ldn_len-1):
        bit_xor = int(ldn[i]) ^ int(ldn[i+4])
        ldn += bit_xor