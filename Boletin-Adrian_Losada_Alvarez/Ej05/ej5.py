from ejercicio5edicion import modulo_editor, \
    objeto_pagina, objeto_bloque, objeto_parrafo, \
    objeto_imagen, objeto_conector, \
    debug_show_document_text_data, test_data, test_config
from ejercicio5idioma import modulo_idioma


class SistemaMonitoreo:
    def __init__(self, documento, idiomas):
        self.documento = documento
        self.eventos = []
        self.revisor = modulo_idioma(idiomas)

    def registrar_evento(self, tipo, datos):
        self.eventos.append({"tipo": tipo, "datos": datos})

    def calcular_estadisticas(self, tipo_evento, clave):
        valores = [evento["datos"][clave] for evento in self.eventos if evento["tipo"] == tipo_evento and clave in evento["datos"]]
        suma = sum(valores)
        promedio = suma / len(valores) if valores else 0
        return {"suma": suma, "promedio": promedio}

    def verificar_alertas(self, tipos_alerta):
        alertas = []
        for evento in self.eventos:
            if evento["tipo"] in tipos_alerta:
                alertas.append(f"Alerta crítica: {evento['tipo']} detectado")
        return alertas

    def revisar_documento(self):
        for pagina in self.documento.pages:
            n_palabras, n_errores = self.documento.revisar_pagina_texto(pagina, self.revisor)
            self.registrar_evento("Revisión", {"palabras": n_palabras, "errores": n_errores})
            if n_errores > 0:
                self.registrar_evento("Error", {"codigo": "ORTOGRAFÍA", "errores": n_errores})

    def mostrar_eventos(self):
        for evento in self.eventos:
            print(evento)