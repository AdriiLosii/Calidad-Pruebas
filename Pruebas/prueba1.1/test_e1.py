import unittest
import e1

class TT(unittest.TestCase):
    def test_metodo_clase_de_prueba(self):
        objeto = e1.c()
        self.assertEqual(objeto.m(), True)


if __name__ == "__main__":
    unittest.main()