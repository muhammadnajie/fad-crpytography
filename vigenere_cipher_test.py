#!/usr/bin/env python3

import unittest
from vigenere_cipher import *

class VigenereCipherTest(unittest.TestCase):
    def test_basic(self):
        testcase = ["negara", "indoin"] #original_key = indo
        expected = "vrjozn"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)

    def test_non_alphabet(self):
        testcase = ["Y4s?", "hehe"]
        expected = "Incorrect message"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)

    def test_empty(self):
        testcase = ["", ""]
        expected = "Incorrect message"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)

    # def test_more_key(self):
    #     testcase = ["transferduitdong", "miskinmiskinmisk"]
    #     expected = "fzsxasqzveqgpwfq"
    #     self.assertEqual(encrypt(testcase[0], testcase[1]), expected)


if __name__ == "__main__":
    unittest.main()