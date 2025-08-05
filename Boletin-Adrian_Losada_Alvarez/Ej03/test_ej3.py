import unittest
from ej3 import JsonLib

class TestJsonLib(unittest.TestCase):
    def setUp(self):
        self.jsonlib = JsonLib()

    def test_valid_json(self):
        # Ejemplos válidos
        self.assertTrue(self.jsonlib.validar("{}"))                                             # Objeto vacío
        self.assertTrue(self.jsonlib.validar('{"a": 0}'))                                       # Número entero
        self.assertTrue(self.jsonlib.validar('{"a": 10.5}'))                                    # Número decimal
        self.assertTrue(self.jsonlib.validar('{"a": ""}'))                                      # Cadena vacía
        self.assertTrue(self.jsonlib.validar('{"a": "txt"}'))                                   # Cadena no vacía
        self.assertTrue(self.jsonlib.validar('{"a": {"b": -1}}'))                               # Objeto anidado
        self.assertTrue(self.jsonlib.validar('{"a": []}'))                                      # Array vacío
        self.assertTrue(self.jsonlib.validar('{"a": [0, 10.5, "0", "", "txt", {"b": -1}]}'))    # Array mixto
        self.assertTrue(self.jsonlib.validar('{"clave uno": "valor uno"}'))                     # Claves con espacios

    def test_invalid_json(self):
        # Ejemplos inválidos
        self.assertFalse(self.jsonlib.validar('"a": 1'))            # Falta objeto externo
        self.assertFalse(self.jsonlib.validar("{a}"))               # Clave sin comillas
        self.assertFalse(self.jsonlib.validar('{"a"}'))             # Falta valor
        self.assertFalse(self.jsonlib.validar('{"a": }'))           # Valor faltante
        self.assertFalse(self.jsonlib.validar('{"a": txt}'))        # Valor sin comillas
        self.assertFalse(self.jsonlib.validar('{"a": 1,}'))         # Coma extra
        self.assertFalse(self.jsonlib.validar('{"a": {"b"}}'))      # Objeto anidado incompleto

    def test_edge_cases(self):
        # Casos límite
        self.assertTrue(self.jsonlib.validar('{"a": [{"b": 1}, {"c": 2}]}'))    # Array de objetos
        self.assertFalse(self.jsonlib.validar(""))                              # Cadena vacía
        self.assertFalse(self.jsonlib.validar(None))                            # Valor nulo
        self.assertTrue(self.jsonlib.validar('{"a": [{"b": -1}, 0, "c"]}'))     # Mezcla en array

if __name__ == "__main__":
    unittest.main()