#!/usr/bin/env python
# encoding: utf-8

class robot():
    def __init__(self, p):
        if not isinstance(p, list):
            raise Exception("Parametro incorrecto")
        if len(p) != 3:
            raise Exception("Longitud incorrecta")
        if not isinstance(p[0], int) or not isinstance(p[1], int) or not isinstance(p[2], int):
            raise Exception("Necesito enteros")
        if p[0]<0 or p[1]<0 or p[2]<0:
            raise Exception("Necesito enteros positivos")
        if p[2]>3:
            raise Exception("Orientacion desconocida")

        self.posicion = (p[0], p[1])
        self.orientacion = p[2]

    def asignar_tablero(self, p, b):
        self.tablero = b
        self.tablero_x = p[0]
        self.tablero_y = p[1]

    def validar(self, cmd):
        if cmd in ["AVANZA", "RETROCEDE", "GIRA.IZQDA", "GIRA.DRCHA", "ESTIRA", "RETRAE", "ABRE", "CIERRA", "FIN"]:
            return True
        else:
            return False

    def mover(self, cmd):
        n = 0
        for i in cmd:
            if self.validar(i):
                # ejecutar el comando i
                if i == "FIN":  # requisito 5
                    break
                # actualizar
                n += 1
            else:
                break

        return n