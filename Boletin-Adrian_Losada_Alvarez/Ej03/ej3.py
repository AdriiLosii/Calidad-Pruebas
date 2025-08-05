class JsonLib:
    def validar(self, json_text):        
        """
        Valida si el texto dado está en formato JSON correcto.

        Parámetros:
            -json_text: El string JSON a validar
        Return:
            - Bool: True si es JSON válido, Falso en caso contario
        """
        if not isinstance(json_text, str):
            return False

        try:
            # Inicializar análisis
            parsed, remainder = self.analizar(json_text.strip())
            return not remainder.strip()  # Asegurarse de que no haya caracteres finales
        except ValueError:
            return False

    def analizar(self, text):
        """
        Analiza recursivamente el texto JSON dado
        """
        text = text.strip()

        if text.startswith("{"):
            return self.analizar_objeto(text)
        elif text.startswith("["):
            return self.analizar_array(text)
        elif text.startswith('"'):
            return self.analizar_string(text)
        elif text in ("True", "False", "None"):
            return text, text[len(text):]
        else:
            return self.analizar_numero(text)

    def analizar_objeto(self, text):
        """
        Analiza el objeto JSON
        """
        if text[0] != "{":
            raise ValueError("Inicio de objeto no válido")
        text = text[1:].strip()

        if text.startswith("}"):
            return {}, text[1:].strip()

        obj = {}
        while text:
            key, text = self.analizar_string(text.strip())
            text = text.strip()

            if not text.startswith(":"):
                raise ValueError("Esperado ':' tras clave")
            text = text[1:].strip()

            value, text = self.analizar(text.strip())
            obj[key] = value
            text = text.strip()

            if text.startswith("}"):
                return obj, text[1:].strip()
            elif text.startswith(","):
                text = text[1:].strip()
            else:
                raise ValueError("Esperado ',' o '}' tras valor")

        raise ValueError("Objeto no cerrado")

    def analizar_array(self, text):
        """
        Analiza el array JSON
        """
        if text[0] != "[":
            raise ValueError("Inicio de array no válido")
        text = text[1:].strip()

        if text.startswith("]"):
            return [], text[1:].strip()

        array = []
        while text:
            value, text = self.analizar(text.strip())
            array.append(value)
            text = text.strip()

            if text.startswith("]"):
                return array, text[1:].strip()
            elif text.startswith(","):
                text = text[1:].strip()
            else:
                raise ValueError("Esperado ',' o ']' tras valor de array")

        raise ValueError("Array no cerrado")

    def analizar_string(self, text):
        """
        Analiza el string JSON
        """
        if not text.startswith('"'):
            raise ValueError("Inicio de string no válido")
        text = text[1:]
        result = []

        while text:
            if text[0] == '"':
                return "".join(result), text[1:]
            elif text[0] == "\\":
                if len(text) < 2:
                    raise ValueError("Secuencia de escape no válida")
                result.append(text[:2])
                text = text[2:]
            else:
                result.append(text[0])
                text = text[1:]

        raise ValueError("String no cerrado")

    def analizar_numero(self, text):
        """
        Analiza el número JSON
        """
        num_chars = "0123456789-+eE."
        index = 0

        while index < len(text) and text[index] in num_chars:
            index += 1

        num_text = text[:index]
        if not num_text:
            raise ValueError("Numero no válido")

        try:
            # Comprobar el formato de número
            if "." in num_text or "e" in num_text or "E" in num_text:
                float(num_text) # Validar como float
            else:
                int(num_text)   # Validar como int
            return num_text, text[index:]

        except ValueError:  # Formato de número incorrecto
            raise ValueError("Formato de número no válido")