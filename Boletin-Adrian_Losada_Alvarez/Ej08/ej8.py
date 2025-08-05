#!/usr/bin/env python3
# encoding: utf-8

class riddle():
    def __init__(self, ring0, ring1, deflector):
        # Validar los anillos:
        # 1. Dimensiones
        if len(ring0) != len(ring1) or len(ring0) != len(deflector) or len(ring1) != len(deflector):
            raise ValueError("Los anillos no tienen las mismas dimensiones.")

        # 2. Validar anillos individualmente
        self._validate_ring(ring0, "Ring0")
        self._validate_ring(ring1, "Ring1")
        self._validate_ring(deflector, "Deflector")

        # 3. Validar consistencia entre anillos
        self._validate_cross_ring([ring0, ring1, deflector])

        self.ring0, self.ring1, self.deflector = ring0, ring1, deflector

    def _ring(self, data, m):
        if m != "":
            for i in data:
                if i[0] == m:
                    return i[1]
        return ""

    def _iring(self, data, m):
        if m != "":
            for i in data:
                if i[1] == m:
                    return i[0]
        return ""

    def _rotate(self, data):
        r = []
        for i in range(1, len(data)):
            r.append((data[i-1][0], data[i][1]))
        r.append((data[len(data)-1][0], data[0][1]))
        return r

    # MODIFICACIÓN: Agregar un método que asegura que todos los caracteres del mensaje son válidos
    def _validate_message(self, txt):
        valid_chars = set(pair[0] for pair in self.ring0)
        if not all(c in valid_chars for c in txt):
            raise ValueError("El mensaje contiene caracteres no válidos.")

    # MODIFICACIÓN: Agregar un método que asegura que los anillos son válidos
    def _validate_ring(self, ring, name):
        VALID_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Definir el conjunto de caracteres válidos
        left_chars = set()
        right_chars = set()

        for left, right in ring:
            # Comprobar caracteres no válidos
            if left not in VALID_CHARS or right not in VALID_CHARS:
                raise ValueError(f"El anillo '{name}' contiene caracteres no válidos: '{left}' o '{right}'.")

            # Comprobar mapeados duplicados
            if left in left_chars or right in right_chars:
                raise ValueError(f"El anillo '{name}' contiene mapeado duplicado: '{left}' o '{right}'.")

            left_chars.add(left)
            right_chars.add(right)

        # Comprobar biyección
        if len(left_chars) != len(ring) or len(right_chars) != len(ring):
            raise ValueError(f"El anillo '{name}' no es válido (no es una biyección).")

    # MODIFICACIÓN: Agregar un método que asegura que haya consistencia de caracteres entre los anillos
    def _validate_cross_ring(self, rings):
        for idx, (ring, name) in enumerate(zip(rings, ["Ring0", "Ring1", "Deflector"])):
            # Obtener todos los caracteres en el anillo actual
            ring_chars = set(pair[0] for pair in ring) | set(pair[1] for pair in ring)

            # Comprobar si cada caracter en este anillo existe en todos los otros anillos
            for char in ring_chars:
                for other_idx, other_ring in enumerate(rings):
                    if idx == other_idx:
                        continue  # Saltar el anillo actual
                    other_chars = set(pair[0] for pair in other_ring) | set(pair[1] for pair in other_ring)
                    if char not in other_chars:
                        raise ValueError(f"El carácter '{char}' de '{name}' no está definido en otro anillo.")

    def encode(self, txt):
        self._validate_message(txt) # Validar el mensaje antes de nada
        r0, r1, d0 = self.ring0.copy(), self.ring1.copy(), self.deflector.copy()
        r, ri = "", 0
        for i in txt:
            r += self._iring(r0, self._iring(r1,
                self._ring(d0,
                self._ring(r1, self._ring(r0, i)))))
            r0, ri = self._rotate(r0), ri+1
            if ri == len(self.ring0):
                ri, r1 = 0, self._rotate(r1)
        return r

    def decode(self, txt):
        self._validate_message(txt) # Validar el mensaje antes de nada
        r0, r1, d0 = self.ring0.copy(), self.ring1.copy(), self.deflector.copy()
        for i in range(len(self.deflector)):
            for j in range(len(self.deflector)):
                if self.deflector[j][1] == self.deflector[i][0]:
                    d0[i] = (self.deflector[j][1], self.deflector[j][0])
                    break
        r, ri = "", 0
        for i in txt:
            r += self._iring(r0, self._iring(r1,
                self._ring(d0,
                self._ring(r1, self._ring(r0, i)))))
            r0, ri = self._rotate(r0), ri+1
            if ri == len(self.ring0):
                ri, r1 = 0, self._rotate(r1)
        return r