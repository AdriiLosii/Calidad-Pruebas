import unittest
from ej8 import riddle

class TestRiddle(unittest.TestCase):
    def test_basic_encoding_decoding(self):
        """
        Test de encoding y decoding básicos.
        """
        rid = riddle(
            [('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'B')],
            [('A', 'A'), ('B', 'C'), ('C', 'E'), ('D', 'D'), ('E', 'B')],
            [('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'C')]
        )
        self.assertEqual(rid.encode("BBE"), "EAC")
        self.assertEqual(rid.decode("EAC"), "BBE")

    def test_full_rotation_ring0(self):
        """
        Test de que el anillo 0 rota correctamente después de cada caracter.
        """
        rid = riddle(
            [('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'B')],
            [('A', 'A'), ('B', 'C'), ('C', 'E'), ('D', 'D'), ('E', 'B')],
            [('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'C')]
        )
        self.assertEqual(rid.encode("AAAAA"), "ADEAD")  # Demostración de rotación
        self.assertEqual(rid.decode("ADEAD"), "AAAAA")

    def test_full_rotation_ring1(self):
        """
        Test de que el anillo 1 rota correctamente después de que el anillo 0 realice una rotación completa.
        """
        rid = riddle(
            [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')],
            [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')],
            [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
        )
        encoded = rid.encode("A" * 10)  # Anillo 0 hace 2 rotaciones completas
        decoded = rid.decode(encoded)
        self.assertEqual(decoded, "A" * 10)

    def test_invalid_message_characters(self):
        """
        Test de valores no válidos.
        """
        rid = riddle(
            [('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'B')],
            [('A', 'A'), ('B', 'C'), ('C', 'E'), ('D', 'D'), ('E', 'B')],
            [('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'C')]
        )
        with self.assertRaises(ValueError):
            rid.encode("AABXZ")  # X y Z no son caracteres válidos
        with self.assertRaises(ValueError):
            rid.decode("BBEXZ")  # X y Z no son caracteres válidos

    def test_non_unique_ring_mappings(self):
        """
        Test de anillos con mapeados únicos.
        """
        with self.assertRaises(ValueError):
            riddle(
                [('A', 'B'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],  # B se mapea 2 veces
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
            )

    def test_empty_message(self):
        """
        Test con texto vacío.
        """
        rid = riddle(
            [('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'B')],
            [('A', 'A'), ('B', 'C'), ('C', 'E'), ('D', 'D'), ('E', 'B')],
            [('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'C')]
        )
        self.assertEqual(rid.encode(""), "")
        self.assertEqual(rid.decode(""), "")

    def test_deflector_reversibility(self):
        """
        Test de que el deflector es reversible.
        """
        rid = riddle(
            [('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'B')],
            [('A', 'A'), ('B', 'C'), ('C', 'E'), ('D', 'D'), ('E', 'B')],
            [('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'C')]
        )
        encoded = rid.encode("ABCDE")
        decoded = rid.decode(encoded)
        self.assertEqual(decoded, "ABCDE")

    def test_ring_0_rotation_multiple_cycles(self):
        """
        Test de rotación múltiple de anillo 0.
        """
        rid = riddle(
            [('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'B')],
            [('A', 'A'), ('B', 'C'), ('C', 'E'), ('D', 'D'), ('E', 'B')],
            [('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'C')]
        )
        encoded = rid.encode("A" * 25)  # Anillo 0 rota 25 veces
        decoded = rid.decode(encoded)
        self.assertEqual(decoded, "A" * 25)

    def test_invalid_ring_definitions(self):
        """
        Test de anillos no válidos.
        """
        with self.assertRaises(ValueError):
            riddle(
                [('A', 'B'), ('B', 'C')],  # Anillo incompleto
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
            )
        with self.assertRaises(ValueError):
            riddle(
                [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')],  # Caracter no válido: F
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
            )
        with self.assertRaises(ValueError):
            riddle(
                [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', '*')],  # Caracter no válido: *
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
                [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
            )

    def test_full_loop_encoding_decoding(self):
        """
        Test de un encoding y decoding completo para un mensaje aleatorio.
        """
        rid = riddle(
            [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')],
            [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')],
            [('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'A'), ('E', 'B')]
        )
        message = "ABCDEABCDEABCDE"
        encoded = rid.encode(message)
        decoded = rid.decode(encoded)
        self.assertEqual(decoded, message)


if __name__ == "__main__":
    unittest.main()