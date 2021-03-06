#!/usr/bin/env python3

from utilz import *
from string import ascii_lowercase
import re

def generate_matrix(key):
    matrix = []
    for i in range(5):
        matrix.append(key[i*5:(i+1)*5])
    return matrix

def adjust_key(key):
    """
    Omit all whitespace, character j, and repeated character.
    """
    no_repeated_character = []
    for char in key:
        if char not in no_repeated_character:
            no_repeated_character.append(char)
    
    for alpha in ascii_lowercase:
        if alpha not in no_repeated_character:
            no_repeated_character.append(alpha)
    adjusted_key = re.sub(r"[j\s]", "", "".join(no_repeated_character))
    return adjusted_key

def convert_bigram(text):
    """
    
    """
    text = re.sub(r"\s", "", text)
    bigram = []
    pointer = 0
    text_len = len(text)
    while(pointer < text_len):
        try:
            if text[pointer] != text[pointer+1]:
                bigram.append(text[pointer] + text[pointer+1])
                pointer = pointer + 2
                continue
            bigram.append(text[pointer] + "x")
            pointer = pointer + 1 
        except:
            bigram.append(text[pointer] + "x")
            pointer = pointer + 1 
    return bigram

def mapping_ref_matrix(matrix):
    mapped_matrix = [None] * 26
    for i in range(len(matrix)):
        for j, char in enumerate(matrix[i]):
            mapped_matrix[ord(char)-97] = f"{i}{j}"
    mapped_matrix[ord('j')-97] = mapped_matrix[ord('i')-97]
    return mapped_matrix

def to_int(args):
    return [int(arg) for arg in args]

def encrypt(bigram, ref_mtrx, ref_mtrx_map):
    cipher = []
    for a,b in bigram:
        a_row, a_col = to_int(ref_mtrx_map[ord(a)-97])
        b_row, b_col = to_int(ref_mtrx_map[ord(b)-97])

        if ref_mtrx[a_row] == ref_mtrx[b_row]:
            a_cipher = ref_mtrx[a_row][(a_col+1)%5]
            b_cipher = ref_mtrx[b_row][(b_col+1)%5]
        elif ref_mtrx[a_col] == ref_mtrx[b_col]:
            a_cipher = ref_mtrx[(a_row+1)%5][a_col]
            b_cipher = ref_mtrx[(b_row+1)%5][b_col]
        else:
            a_cipher = ref_mtrx[a_row][b_col]
            b_cipher = ref_mtrx[b_row][a_col]
        cipher.append(f"{a_cipher}{b_cipher}")

    return " ".join(cipher)

def decrypt(bigram, ref_mtrx, ref_mtrx_map):
    pass

def main():
    # type = input("[e,d]?")
    # key = input("key: ")
    key = "jalan ganesha sepuluh"
    key = adjust_key(key)
    ref_matrix = generate_matrix(key)
    plaintext = "temui ibu nanti malam "
    # plaintext = "kirito"
    plaintext = re.sub("j", "i", plaintext)
    ref_bigram = convert_bigram(plaintext)
    ref_matrix_map = mapping_ref_matrix(ref_matrix)
    target_text = encrypt(ref_bigram, ref_matrix, ref_matrix_map)
    print(target_text)

main()