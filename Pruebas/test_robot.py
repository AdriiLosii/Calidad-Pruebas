#!/usr/bin/env python
# encoding: utf-8

import unittest
from robot import robot

class T1(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_01(self):
        with self.assertRaises(Exception): robot()
        with self.assertRaises(Exception): robot((1, 2, 3))
        with self.assertRaises(Exception): robot("1, 2, 3")
        with self.assertRaises(Exception): robot([])
        with self.assertRaises(Exception): robot([1])
        with self.assertRaises(Exception): robot([1, 2, 3, 4])
        self.assertTrue(isinstance(robot([1, 2, 3]), robot))


    def test_02(self):
        r = robot([1, 2, 3])
        self.assertEqual(r.posicion, (1, 2))

        with self.assertRaises(Exception): r2 = robot([1.1, 2.5, 3])
        with self.assertRaises(Exception): r2 = robot([-10, -20, 3])

    def test_03(self):
        r = robot([1, 2, 3])
        self.assertEqual(r.orientacion, 3)

        with self.assertRaises(Exception): r2 = robot([1, 2, 3.5])
        with self.assertRaises(Exception): r2 = robot([1, 2, -1])
        with self.assertRaises(Exception): r2 = robot([1, 2, 4])

    def test_04(self):
        r = robot([1, 2, 3])
        self.assertTrue(r.validar("AVANZA"))
        self.assertFalse(r.validar("SALTA"))
        for comando in ["AVANZA", "RETROCEDE", "GIRA.IZQDA", "GIRA.DRCHA", "ESTIRA", "RETRAE", "ABRE", "CIERRA", "FIN"]:
            self.assertTrue(r.validar(comando))

    def test_05(self):
        r = robot([1, 2, 3])
        cmd1 = ["AVANZA", "AVANZA", "GIRA.DRCHA", "FIN"]
        cmd2 = ["AVANZA", "AVANZA", "GIRA.DRCHA", "FIN", "AVANZA", "GIRA.IZQDA"]
        self.assertEqual(r.mover(cmd1), 3)
        self.assertEqual(r.mover(cmd2), 3)

    def test_06(self):
        pass

    def test_07(self):
        r = robot([1, 2, 3])
        r.asignar_tablero([4, 4, 4],
            [
                [
                    [0, 1, 0, 1],
                    [0, 0, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 1, 0]
                ],
                [
                    [0, 0, 0, 1],
                    [0, 0, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 1, 0]
                ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ]
            ])
        r.mover("[RETROCEDE]")
        self.assertEqual(r.posicion, (1, 3))


if __name__ == "__main__":
    unittest.main()