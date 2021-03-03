#!/usr/bin/env python3

import math
import re

def to_file(msg):
    with open("result.txt", "w") as f:
        f.write(msg)

def customize_text(type, source_text, target_text):
    if target_text == None:
        return "Incorrect type"
    return f"{type}({source_text}) = {target_text}"

def is_valid(text):
    return re.match(r"[a-z]+", text)

def encrypt(plain_text, key):
    if not is_valid(plain_text):
        return "Incorrect message (Text only)"

    int_key = int(key)
    ciphertext = [chr((ord(char)-97+int_key)%26+97) for char in plain_text]
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    if not is_valid(ciphertext):
        return "Incorrect message (Text only)"

    int_key = int(key)
    ciphertext = [chr((ord(char)-97-int_key)%26+97) for char in ciphertext]
    return "".join(ciphertext)


def main():
    type = input("[e,d]?")
    source_text = input("from: ")
    target_text = None
    if type == "e":
        print("encrypt")
    elif type == "d":
        print("decrypt")

    msg = customize_text(type, source_text, target_text)
    to_file(msg)

#main()
    
    