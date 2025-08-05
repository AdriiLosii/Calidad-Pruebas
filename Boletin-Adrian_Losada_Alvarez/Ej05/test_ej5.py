import unittest
from ej5 import *

class TestSistemaMonitoreo(unittest.TestCase):
    def setUp(self):
        pages_text_data = [
        objeto_pagina("primera página", [
            objeto_bloque(
                [objeto_parrafo("contenido del bloque de texto A")],
                (10, 10, 10, 10)
            ),
            objeto_bloque([
                    objeto_parrafo("contenido del bloque de texto B"),
                    objeto_parrafo("contenido del bloque de texto B"),
                    objeto_parrafo("contenido del bloque de texto B")
                ],
                (30, 30, -1, -1)
            ),
            objeto_bloque(
                [objeto_parrafo("contenido del bloque de texto C")],
                (40, 40, -1, -1)
            ),
        ]),
        objeto_pagina("segunda página", [
            objeto_bloque([objeto_parrafo("<strong>text block</strong> content", lang="en_US")]),
            objeto_bloque([objeto_parrafo("<em>text block</em> content", lang="en_US")]),
            objeto_bloque([objeto_parrafo("<u>text block</u> content", lang="en_US")])
        ]),
        objeto_pagina("tercera página", images=[
            objeto_imagen("logo1.svg", (0, 0, -1, -1)),
            objeto_imagen("logo2.svg", (40, 40, 10, 10))
        ])]
        self.sistema = SistemaMonitoreo(pages_text_data, {"default_lang":"es_ES"})

    def test_registro_eventos(self):
        # Registrar eventos y verificar el conteo
        self.sistema.registrar_evento("Movimiento", {"distancia": 5})
        self.sistema.registrar_evento("Movimiento", {"distancia": 10})
        self.sistema.registrar_evento("Error", {"codigo": 404})
        self.assertEqual(len(self.sistema.eventos), 3)

    def test_estadisticas(self):
        # Calcular estadísticas basadas en eventos
        self.sistema.registrar_evento("Movimiento", {"distancia": 5})
        self.sistema.registrar_evento("Movimiento", {"distancia": 10})
        self.sistema.registrar_evento("Movimiento", {"distancia": 15})
        stats = self.sistema.calcular_estadisticas("Movimiento", "distancia")
        self.assertEqual(stats["suma"], 30)
        self.assertEqual(stats["promedio"], 10)

    def test_alertas(self):
        # Generar alertas basadas en condiciones críticas
        self.sistema.registrar_evento("Error", {"codigo": 404})
        self.sistema.registrar_evento("Error", {"codigo": 500})
        alertas = self.sistema.verificar_alertas(["Error"])
        self.assertIn("Alerta crítica: Error detectado", alertas)

    def test_sistema_integrado(self):
        # Probar todas las funcionalidades juntas
        self.sistema.registrar_evento("Movimiento", {"distancia": 10})
        self.sistema.registrar_evento("Error", {"codigo": 500})
        stats = self.sistema.calcular_estadisticas("Movimiento", "distancia")
        alertas = self.sistema.verificar_alertas(["Error"])
        self.assertEqual(stats["suma"], 10)
        self.assertIn("Alerta crítica: Error detectado", alertas)

if __name__ == "__main__":
    unittest.main()