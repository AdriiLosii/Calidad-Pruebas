#!/usr/bin/env python
# encoding: utf-8

import unittest
from ej1 import invertir

class ObjTesting(unittest.TestCase):
    # req 1
    def test_cadena_vacia(self):
        #self.assertEqual(invertir(""))
        with self.assertRaises(Exception()):
            invertir("")

    # req 2
    def test_una_letra(self):
        self.assertEqual(invertir("a"), "a")
        self.assertEqual(invertir("0"), "0")
        self.assertNotEqual(invertir("a"), "")
        self.assertNotEqual(invertir(""), "")

    # req 3
    # req 4

if __name__ == "__main__":
    unittest.main()