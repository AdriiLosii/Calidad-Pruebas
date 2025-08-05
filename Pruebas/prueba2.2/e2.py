"""class moneda():
    def __init__(self, txt):
        if txt == "": raise Exception()
        if not isinstance(txt, str): raise Exception()
        self.unidades = txt

    def cantidad(self, n):
        if not isinstance(n, int) and not isinstance(n, float): raise Exception()
        if n < 0: raise Exception()
        self.valores = n"""
        
class moneda():
    etq = None
    nnn = 1
    def __init__(self, txt):
        if txt == "":
            raise "Error, no hay etiqueta"
        self.etq = txt.strip()

    def asignar(self, valor):
        if valor == 10:
            self.nnn = 10