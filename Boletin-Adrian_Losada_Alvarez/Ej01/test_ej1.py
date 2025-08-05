import unittest
from ej1 import a2r, r2a

class TestConversionNumerosRomanos(unittest.TestCase):
    # Pruebas para a2r (arábigo a romano)
    def test_a2r_basico(self):
        self.assertEqual(a2r(1), "I")
        self.assertEqual(a2r(2), "II")
        self.assertEqual(a2r(4), "IV")
        self.assertEqual(a2r(5), "V")
        self.assertEqual(a2r(9), "IX")
        self.assertEqual(a2r(40), "XL")
        self.assertEqual(a2r(90), "XC")
        self.assertEqual(a2r(400), "CD")
        self.assertEqual(a2r(900), "CM")
        self.assertEqual(a2r(3000), "MMM")
    
    def test_a2r_limites(self):
        self.assertEqual(a2r(1), "I")
        with self.assertRaises(ValueError):     # Excepción si supera el límite inferior (No hay representación romana para 0)
            a2r(0)

        self.assertEqual(a2r(3000), "MMM")
        with self.assertRaises(ValueError):     # Excepción si supera el límite superior (Complejidad)
            a2r(3001)

    def test_a2r_error(self):
        with self.assertRaises(ValueError):     # Excepción si el número introducido es negativo
            a2r(-1)
        with self.assertRaises(ValueError):     # Excepción si el número introducido es decimal
            a2r(2.5)

    # Pruebas para r2a (romano a arábigo)
    def test_r2a_basico(self):
        self.assertEqual(r2a("I"), 1)
        self.assertEqual(r2a("II"), 2)
        self.assertEqual(r2a("IV"), 4)
        self.assertEqual(r2a("V"), 5)
        self.assertEqual(r2a("IX"), 9)
        self.assertEqual(r2a("XL"), 40)
        self.assertEqual(r2a("XC"), 90)
        self.assertEqual(r2a("CD"), 400)
        self.assertEqual(r2a("CM"), 900)
        self.assertEqual(r2a("MMM"), 3000)

    def test_r2a_malformado(self):
        with self.assertRaises(ValueError):     # Excepción si no es válido (Más de 3 repeticiones consecutivas no son válidas)
            r2a("IIII")  
        with self.assertRaises(ValueError):     # Excepción si no es válido (Secuencia no es válida)
            r2a("VX")

    def test_r2a_mixto(self):
        self.assertEqual(r2a("MCMXCIV"), 1994)  # Caso complejo
        self.assertEqual(r2a("XCIX"), 99)

if __name__ == "__main__":
    unittest.main()