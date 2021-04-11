""""
Electronic Code Book Algorithm
w/ Rule: E(P) = (P ^ key) << 2 (Cyclic)
"""

from util import *

def encrypt(plain_text, key):
    plain_bins = text_to_bin(plain_text)
    
    encrypted = []
    for plain_bin in plain_bins:
        converted = xor_two_bins(plain_bin, key)
        shifted = left_shift_cyclic(converted, 2)
        encrypted.append(shifted)
        
    cipher_text = bins_to_string(encrypted)
    return cipher_text

def decrypt(cipher_text, key):
    cipher_bins = text_to_bin(cipher_text) # list of str

    decrypted = []
    for cipher_bin in cipher_bins:
        shifted = right_shift_cyclic(cipher_bin, 2)
        converted = xor_two_bins(shifted, key)
        decrypted.append(converted)

    plain_text = bins_to_string(decrypted)
    return plain_text
    

def main():
    """Assumption 1 block = 8 bit"""
    # my last 3 digit student identity in ascii
    plain_text = "131" #dummy
    key = "11011011"
    cipher_text = encrypt(plain_text, key)
    print(cipher_text)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)

main()