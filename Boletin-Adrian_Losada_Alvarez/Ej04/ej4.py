class Movil:
    """
    Representa el móvil en el escenario.
    """
    def __init__(self, posicion=(0, 0), orientacion='N', altura_brazo=0, longitud_brazo=0, pinza_abierta=True, escenario=None):
        self.posicion = list(posicion)  # [x, y]
        self.orientacion = orientacion  # 'N', 'E', 'S', 'O'
        self.altura_brazo = altura_brazo
        self.longitud_brazo = longitud_brazo
        self.pinza_abierta = bool(pinza_abierta)
        self.escenario = escenario

    def comando(self, orden):
        try:
            if orden.startswith("FORWARD"):
                self.mover(int(orden.split()[1]))
            elif orden.startswith("SHIFT"):
                self.deslizar(int(orden.split()[1]))
            elif orden == "LEFT":
                self.girar(-1)
            elif orden == "RIGHT":
                self.girar(1)
            elif orden.startswith("ELEVATE"):
                self.altura_brazo += int(orden.split()[1])
            elif orden.startswith("EXTEND"):
                self.longitud_brazo += int(orden.split()[1])
            elif orden == "GRAB":
                self.pinza_abierta = False
            elif orden == "RELEASE":
                self.pinza_abierta = True
            else:
                raise ValueError(f"Comando desconocido: {orden}")
        except Exception as e:
            raise ValueError(f"Error al ejecutar el comando '{orden}': {e}")

    def mover(self, pasos):
        direcciones = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'O': (0, -1)}
        dx, dy = direcciones[self.orientacion]
        for _ in range(abs(pasos)):
            nueva_pos = [self.posicion[0] + dx * (1 if pasos > 0 else -1), self.posicion[1] + dy * (1 if pasos > 0 else -1)]
            if not self.escenario.detectar_colision(nueva_pos):
                self.posicion = nueva_pos
            else:
                break

    def deslizar(self, pasos):
        direcciones = {'N': (0, 1), 'E': (-1, 0), 'S': (0, -1), 'O': (1, 0)}
        dx, dy = direcciones[self.orientacion]
        for _ in range(abs(pasos)):
            nueva_pos = [self.posicion[0] + dx * (1 if pasos > 0 else -1), self.posicion[1] + dy * (1 if pasos > 0 else -1)]
            if not self.escenario.detectar_colision(nueva_pos):
                self.posicion = nueva_pos
            else:
                break

    def girar(self, direccion):
        orientaciones = ['N', 'E', 'S', 'O']
        idx = orientaciones.index(self.orientacion)
        self.orientacion = orientaciones[(idx + direccion) % 4]

class Escenario:
    """
    Representa el escenario 3D donde se mueve el móvil.
    """
    def __init__(self, dimensiones, bloques):
        self.dimensiones = {
            "xmin": -dimensiones[0] // 2 + 1,
            "xmax": dimensiones[0] // 2,
            "ymin": -dimensiones[1] // 2 + 1,
            "ymax": dimensiones[1] // 2,
            "zmax": dimensiones[2]
        }
        self.bloques = bloques

    def detectar_colision(self, posicion):
        x, y = posicion

        # Comprueba si la posición está dentro de los límites
        if not (self.dimensiones["xmin"] <= x <= self.dimensiones["xmax"] and
                self.dimensiones["ymin"] <= y <= self.dimensiones["ymax"]):
            return True  # Fuera de los límites

        # Convierte las coordenadas a indices de la matriz
        x_idx = x - self.dimensiones["xmin"]
        y_idx = y - self.dimensiones["ymin"]

        # Comprueba si hay un bloque en esta posición en todas las capas
        for layer in self.bloques:
            if 0 <= x_idx < len(layer) and 0 <= y_idx < len(layer[0]):
                if layer[x_idx][y_idx] == 1:
                    return True  # Bloque detectado
        return False  # No se ha detectado bloque

    def actualizar(self):
        for z in range(len(self.bloques) - 1, 0, -1):
            for x in range(len(self.bloques[z])):
                for y in range(len(self.bloques[z][0])):
                    if self.bloques[z][x][y] == 1 and self.bloques[z - 1][x][y] == 0:
                        self.bloques[z][x][y] = 0
                        self.bloques[z - 1][x][y] = 1

class Simulacion:
    """
    Representa la simulación completa que coordina el móvil y el escenario.
    """
    def __init__(self, movil, escenario, comandos):
        self.movil = movil
        self.escenario = escenario
        self.comandos = comandos.split(", ")

    def ejecutar(self):
        try:
            for comando in self.comandos:
                self.movil.comando(comando)
                self.escenario.actualizar()
            return True
        except Exception as e:
            print(f"Error durante la simulación: {e}")
            return False