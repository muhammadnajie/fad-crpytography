#!/usr/bin/env python3

from utilz import *

def encrypt(plaintext, key):
    if not is_valid(plaintext):
        return "Incorrect message"

    int_key = int(key)
    ciphertext = [chr((ord(char)-97+int_key)%26+97) for char in plaintext]
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    if not is_valid(ciphertext):
        return "Incorrect message"

    int_key = int(key)
    ciphertext = [chr((ord(char)-97-int_key)%26+97) for char in ciphertext]
    return "".join(ciphertext)


def main():
    type = input("[e,d]?")
    source_text = input("text: ")
    key = input("key: ")
    target_text = None
    if type == "e":
        target_text = encrypt(source_text, key)
    elif type == "d":
        target_text = decrypt(source_text, key)

    msg = customize_text(type, source_text, target_text)
    status = to_file("caeshar_cipher_result.txt", msg)
    print(status)

main()
    
    