#!/usr/bin/env python
# encoding: utf-8

import unittest
from e2 import moneda

class R1(unittest.TestCase):
    def test_crear_moneda_con_texto(self):
        # Captura de error basica
        with self.assertRaises(Exception):
            moneda()
        # Esto es una mejora a la captura de error anterior, de esta manera podemos indicar el tipo de error
        with self.assertRaises(Exception) as c:
            moneda("")
            self.assertEqual(str(c.exception), "no hay etiqueta")
        self.assertIsInstance(moneda("etiqueta"), moneda)
    def test_moneda_con_notexto(self):
        with self.assertRaises(Exception) as c:
            moneda(0)
            self.assertEqual(str(c.exception), "no hay etiqueta")
        with self.assertRaises(Exception) as c:
            moneda(None)
            self.assertEqual(str(c.exception), "no hay etiqueta")
        with self.assertRaises(Exception) as c:
            moneda(list(1,2,3))
            self.assertEqual(str(c.exception), "no hay etiqueta")

class R2(unittest.TestCase):
    def test_evaluar_etiqueta(self):
        x = moneda("Abc")
        self.assertEqual(x.etq, "Abc")
        self.assertNotEqual(x.etq, "")
        self.assertNotEqual(x.etq, "ABC")
        self.assertNotEqual(x.etq, "abc")
        x = moneda("abc")
        self.assertEqual(x.etq, "abc")
        x = moneda("ABC")
        self.assertEqual(x.etq, "ABC")

    def test_evaluar_etiqueta_con_espacios(self):
        x = moneda(" abc")
        self.assertEqual(x.etq, "abc")
        self.assertNotEqual(x.etq, " abc")
        x = moneda(" abc  ")
        self.assertEqual(x.etq, "abc")

class R3(unittest.TestCase):
    def test_asignar_valor_numerico(self):
        # euro = moneda("EUR")
        # euro(10) -> euro.asignar(10)
        # print(euro.asignar(10)) -> euro.valor()

        euro = moneda("EUR")
        euro.asignar(10)
        self.assertEqual(euro.nnn, "10")
        euro.asignar(20)
        self.assertEqual(euro.nnn, "20")
        with self.assertRaises(Exception) as c:
            euro.asignar(-1)
            self.assertNotEqual(euro.nnn, -1)
            self.assertEqual(str(c.exception), "valores negativos")



if __name__ == '__main__':
    unittest.main()