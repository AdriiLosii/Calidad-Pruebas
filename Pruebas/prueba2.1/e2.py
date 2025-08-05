class moneda():
    def __init__(self, txt):
        if txt == "": raise Exception()
        if not isinstance(txt, str): raise Exception()
        self.unidades = txt

    def cantidad(self, n):
        if not isinstance(n, int) and not isinstance(n, float): raise Exception()
        if n < 0: raise Exception()
        self.valores = n