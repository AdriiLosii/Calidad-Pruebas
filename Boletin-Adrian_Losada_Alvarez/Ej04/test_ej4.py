import unittest
from ej4 import Movil, Escenario, Simulacion

class TestSimulacion(unittest.TestCase):
    def setUp(self):
        # Configuración básica para pruebas
        self.escenario = Escenario((5, 5, 4), [[[0 for _ in range(5)] for _ in range(5)] for _ in range(4)])
        self.movil = Movil((0, 0), 'N', 0, 0, True, self.escenario)

    # MOVIL Tests
    def test_movil_inputs(self):
        # Posición inicial correcta
        self.assertEqual(self.movil.posicion, [0, 0])
        # Orientación inicial correcta
        self.assertEqual(self.movil.orientacion, 'N')
        # Estado inicial del brazo
        self.assertEqual(self.movil.altura_brazo, 0)
        self.assertEqual(self.movil.longitud_brazo, 0)
        self.assertTrue(self.movil.pinza_abierta)

    def test_movil_operations(self):
        # FORWARD - Moverse adelante (positivo)
        self.movil.comando("FORWARD 2")
        self.assertEqual(self.movil.posicion, [2, 0])
        # FORWARD - Moverse atrás (negativo)
        self.movil.comando("FORWARD -2")
        self.assertEqual(self.movil.posicion, [0, 0])
        # FORWARD - Valores incorrectos (decimal)
        with self.assertRaises(ValueError): self.movil.comando("FORWARD 0.25")
        # FORWARD - Valores incorrectos (caracter)
        with self.assertRaises(ValueError): self.movil.comando("FORWARD A")

        # SHIFT - Moverse adelante (positivo)
        self.movil.comando("SHIFT 2")
        self.assertEqual(self.movil.posicion, [0, 2])
        # SHIFT - Moverse atrás (negativo)
        self.movil.comando("SHIFT -2")
        self.assertEqual(self.movil.posicion, [0, 0])
        # SHIFT - Valores incorrectos (decimal)
        with self.assertRaises(ValueError): self.movil.comando("SHIFT 0.25")
        # SHIFT - Valores incorrectos (caracter)
        with self.assertRaises(ValueError): self.movil.comando("SHIFT A")

        # RIGHT - Girar a la derecha
        self.movil.comando("RIGHT")
        self.assertEqual(self.movil.orientacion, 'E')

        # LEFT - Girar a la izquierda
        self.movil.comando("LEFT")
        self.assertEqual(self.movil.orientacion, 'N')

        # ELEVATE - Elevar brazo (positivo)
        self.movil.comando("ELEVATE 2")
        self.assertEqual(self.movil.altura_brazo, 2)
        # ELEVATE - Descender brazo (negativo)
        self.movil.comando("ELEVATE -2")
        self.assertEqual(self.movil.altura_brazo, 0)
        # ELEVATE - Valores incorrectos (decimal)
        with self.assertRaises(ValueError): self.movil.comando("ELEVATE 0.5")
        # ELEVATE - Valores incorrectos (caracter)
        with self.assertRaises(ValueError): self.movil.comando("ELEVATE B")

        # EXTEND - Extender brazo (positivo)
        self.movil.comando("EXTEND 1")
        self.assertEqual(self.movil.longitud_brazo, 1)
        # EXTEND - Contraer brazo (negativo)
        self.movil.comando("EXTEND -1")
        self.assertEqual(self.movil.longitud_brazo, 0)
        # EXTEND - Valores incorrectos (decimal)
        with self.assertRaises(ValueError): self.movil.comando("EXTEND 1.5")
        # EXTEND - Valores incorrectos (caracter)
        with self.assertRaises(ValueError): self.movil.comando("EXTEND C")

        # GRAB - Cerrar pinza
        self.movil.comando("GRAB")
        self.assertFalse(self.movil.pinza_abierta)

        # RELEASE - Abrir pinza
        self.movil.comando("RELEASE")
        self.assertTrue(self.movil.pinza_abierta)

    # ESCENARIO Tests
    def test_escenario_inputs(self):
        # Dimensiones correctas
        self.assertEqual(self.escenario.dimensiones["xmin"], -2)
        self.assertEqual(self.escenario.dimensiones["xmax"], 2)
        self.assertEqual(self.escenario.dimensiones["ymin"], -2)
        self.assertEqual(self.escenario.dimensiones["ymax"], 2)
        self.assertEqual(self.escenario.dimensiones["zmax"], 4)

        # Matriz de bloques vacía
        self.assertTrue(all(all(all(block == 0 for block in row) for row in layer) for layer in self.escenario.bloques))

    def test_escenario_espacios(self):
        # Definir un bloque en la posición [2, 2]
        x_idx = 2 - self.escenario.dimensiones["xmin"]
        y_idx = 2 - self.escenario.dimensiones["ymin"]
        self.escenario.bloques[0][x_idx][y_idx] = 1

        # Comprobar la colisión en [2, 2]
        self.assertTrue(self.escenario.detectar_colision([2, 2]))

    # SIMULACION Tests
    def test_simulacion_tiene_movil(self):
        self.assertIsNotNone(self.movil)

    def test_comandos_conocidos(self):
        # Comandos válidos
        comandos_validos = ["FORWARD 2", "FORWARD -1", "SHIFT 1", "SHIFT -3", "LEFT", "RIGHT", "ELEVATE 3", "ELEVATE -2", "EXTEND 2", "EXTEND -1", "GRAB", "RELEASE"]
        for comando in comandos_validos:
            try:
                self.movil.comando(comando)
            except Exception as e:
                self.fail(f"Comando válido '{comando}' falló con error: {e}")

        # Comando desconocido
        with self.assertRaises(Exception): self.movil.comando("DESCONOCIDO")

    def test_simulacion_responde_a_comandos(self):
        comandos = "FORWARD 2, LEFT, FORWARD 1, ELEVATE 1, GRAB"
        simulacion = Simulacion(self.movil, self.escenario, comandos)
        self.assertTrue(simulacion.ejecutar())

        # Comprobación de estado final
        self.assertEqual(self.movil.posicion, [2, -1])
        self.assertEqual(self.movil.orientacion, 'O')
        self.assertEqual(self.movil.altura_brazo, 1)
        self.assertFalse(self.movil.pinza_abierta)

if __name__ == "__main__":
    unittest.main()