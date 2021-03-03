#!/usr/bin/env python3

import unittest
from caesar_cipher import encrypt, decrypt

class CaesarCipherTest(unittest.TestCase):
    def test_encrypt_basic(self):
        testcase = ["abc", "2"]
        expected = "cde"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)

    def test_encrypt_overlap(self):
        testcase = ["zxc", "2"]
        expected = "bze"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)

    def test_encrypt_with_non_alphabet(self):
        testcase = ["4l4y", "2"]
        expected = "Incorrect message (Text only)"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)

    def test_decrypt_basic(self):
        testcase = ["cde", "2"]
        expected = "abc"
        self.assertEqual(decrypt(testcase[0], testcase[1]), expected)

    def test_decrypt_overlap(self):
        testcase = ["bze", "2"]
        expected = "zxc"
        self.assertEqual(decrypt(testcase[0], testcase[1]), expected)

    def test_decrypt_with_non_alphabet(self):
        testcase = ["/akoa488@@.", "2"]
        expected = "Incorrect message (Text only)"
        self.assertEqual(decrypt(testcase[0], testcase[1]), expected)

if __name__ == '__main__':
    unittest.main()