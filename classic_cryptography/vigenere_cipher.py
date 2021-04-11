#!/usr/bin/env python3

from math import ceil
from string import ascii_lowercase
from utilz import *
import sys

def generate_matrix():
    matrix = []
    for c in ascii_lowercase:
        m_i = []
        base = ord(c)-97
        for j in range(26):
            base_shift_j = (base+j)%26
            alphabet = chr(base_shift_j+97)
            m_i.append(alphabet)
        matrix.append(m_i)
    return matrix

def adjust_key(text, key):
    """
    If the given key length less than text length, 
    then repeat the key periodically
    """
    text_len = len(text)
    key_len = len(key)
    if key_len > text_len:
        return key
    
    key = key*(ceil(text_len/key_len))
    return key[:text_len]

def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += CIPHER_MATRIX[ord(plaintext[i])-97][ord(key[i])-97]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        asc = ord(ciphertext[i])-ord(key[i])
        if asc < 0:
            asc = asc+26
        plaintext += chr(asc%26+97)
    return plaintext

def main():
    """
    Limitation: Only processes text that contains alphabet only
    Assumption: The input file contains only one line of text 
    """
    type = input("[e,d]?")
    key = input("key: ")

    correct_type = check_type(type)
    if not correct_type:
        type = False

    if not alphabet_only(key):
        key = False

    try:
        with open("source.txt", "r") as f:
            source_text = f.readline()
            if not alphabet_only(source_text):
                source_text = False
                target_text = 'Incorrect message'
    except:
        sys.exit("Failed read source file")


    if not all([type, key, source_text]):
        sys.exit("Operation failed.")
    
    key = adjust_key(source_text, key)
    if type == "e":
        target_text = encrypt(source_text, key)
    elif type == "d":
        target_text = decrypt(source_text, key)
    msg = customize_text(type, source_text, target_text)
    status = to_file("vigenere_cipher_result.txt", msg)
    print(status)

CIPHER_MATRIX = generate_matrix()
main()