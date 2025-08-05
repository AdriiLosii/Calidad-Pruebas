import unittest
from e2 import moneda

class T1(unittest.TestCase):
    def test_crear_moneda_1(self):
        euro = moneda("EUR")
        self.assertIsInstance(euro, moneda)

    def test_crear_moneda_2(self):
        with self.assertRaises(Exception):
            euro = moneda("")

    def test_crear_moneda_3(self):
        with self.assertRaises(Exception):
            euro = moneda(2)
        with self.assertRaises(Exception):
            euro = moneda(2.0)
        with self.assertRaises(Exception):
            euro = moneda([])

    def test_crear_moneda_4(self):
        p = moneda("PESETA")
        self.assertNotEqual(p.unidades, "")
        self.assertNotEqual(p.unidades, "EURO")
        self.assertEqual(p.unidades, "PESETA")


class T2(unittest.TestCase):
    def test_darle_valor_1(self):
        euro = moneda("EURO")
        euro.cantidad(10)
        self.assertEqual(euro.valores, 10)

    def test_darle_valor_2(self):
        euro = moneda("EURO")
        euro.cantidad(0)
        self.assertEqual(euro.valores, 0)
        with self.assertRaises(Exception):
            euro.cantidad(-1)

    def test_darle_valor_3(self):
        euro = moneda("EURO")
        euro.cantidad(20)
        self.assertEqual(euro.valores, 20)
        euro.cantidad(20.5)
        self.assertEqual(euro.valores, 20.5)
        with self.assertRaises(Exception):
            euro.cantidad("0")
        with self.assertRaises(Exception):
            euro.cantidad([])
        with self.assertRaises(Exception):
            euro.cantidad(None)
        

    if __name__ == "__main__":
        unittest.main()