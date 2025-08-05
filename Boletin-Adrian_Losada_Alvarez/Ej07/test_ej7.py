import unittest
from ej7 import es_dni

class TestEsDNI(unittest.TestCase):
    def test_formato_valido(self):
        self.assertTrue(es_dni("IDESPBAA000589599999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7"))

    def test_pais_no_valido(self):
        with self.assertRaises(ValueError):
            es_dni("IDFRAAA000589599999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7")

    def test_letras_no_mayusculas(self):
        self.assertFalse(es_dni("IDESPBAA000589599999999r<<<<<<8001014F2501017ESP<<<<<<<<<<<7"))

    def test_numero_soporte_invalido(self):
        with self.assertRaises(ValueError):
            es_dni("IDESPAA000589599999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7")

    def test_fecha_no_valida(self):
        self.assertFalse(es_dni("IDESPBAA000589599999999R<<<<<<8001014F9999997ESP<<<<<<<<<<<7"))

    def test_con_apellidos(self):
        self.assertTrue(es_dni("IDESPBAA000589599999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7ESPANOLA<ESPANOLA<<CARMEN<<<<<"))

    def test_valores_maximos(self):
        self.assertTrue(es_dni("IDESPJJJ999999799999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<3"))

    def test_valores_minimos(self):
        self.assertTrue(es_dni("IDESPAAA000000099999999R<<<<<<0001018F2501017ESP<<<<<<<<<<<5"))

    def test_codigo_control_incorrecto(self):
        self.assertFalse(es_dni("IDESPBAA000589599999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<0"))

    def test_sin_pais(self):
        with self.assertRaises(ValueError):
            es_dni("BAA000589599999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7")

    def test_sin_control_inicial(self):
        with self.assertRaises(ValueError):
            es_dni("IDESPBAA000589599999999<<<<<<8001014F2501017ESP<<<<<<<<<<<7")

    def test_longitud_incorrecta(self):
        with self.assertRaises(ValueError):
            es_dni("IDESPBAA000589599999")
        with self.assertRaises(ValueError):
            es_dni("IDESPBAA00058959")
        with self.assertRaises(ValueError):
            es_dni("IDESPBAA000589599999999R<<<<<<")

    def test_caracteres_invalidos(self):
        self.assertFalse(es_dni("IDESPBAA00058@5-9999999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7"))
        self.assertFalse(es_dni("IDESPBAA00058959999*999R<<<<<<8001014F2501017ESP<<<<<<<<<<<7"))

    def test_fechas_limite(self):
        # # Fecha de nacimiento en límite inferior (00-01-01)
        self.assertTrue(es_dni("IDESPBAA000589599999999R<<<<<<0001018F2501017ESP<<<<<<<<<<<5"))
        # # Fecha de nacimiento en límite superior (99-12-31)
        self.assertTrue(es_dni("IDESPBAA000589599999999R<<<<<<9912315F2501017ESP<<<<<<<<<<<5"))

        # Fecha de expedición en límite inferior (00-01-01)
        self.assertTrue(es_dni("IDESPBAA000589599999999R<<<<<<8001014F0001018ESP<<<<<<<<<<<1"))
        # Fecha de expedición en límite superior (99-12-31)
        self.assertTrue(es_dni("IDESPBAA000589599999999R<<<<<<8001014F9912315ESP<<<<<<<<<<<5"))

    def test_fechas_invalidas(self):
        # Fecha de nacimiento no válida (Mes 13)
        self.assertFalse(es_dni("IDESPBAA000589599999999R<<<<<<8013014F2501017ESP<<<<<<<<<<<7"))
        # Fecha de expedición no válida (Día 33)
        self.assertFalse(es_dni("IDESPBAA000589599999999R<<<<<<8001014F2513327ESP<<<<<<<<<<<7"))

    def test_nif_letra_incorrecta(self):
        # Número NIF correcto pero letra incorrecta
        self.assertFalse(es_dni("IDESPBAA000589599999999X<<<<<<8001014F2501017ESP<<<<<<<<<<<7"))


if __name__ == "__main__":
    unittest.main()