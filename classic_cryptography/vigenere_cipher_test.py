#!/usr/bin/env python3

import unittest
from vigenere_cipher import *

class VigenereCipherTest(unittest.TestCase):
    def test_encrypt(self):
        testcase = ["negara", "indoin"] #original_key = indo
        expected = "vrjozn"
        self.assertEqual(encrypt(testcase[0], testcase[1]), expected)
    



if __name__ == "__main__":
    unittest.main()