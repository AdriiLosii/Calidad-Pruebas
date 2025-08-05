class auth():
    def read_permission(self):
        pass
    def write_permission(self):
        pass

class auth_by_pin(auth):
    data = []
    remember = False
    validated = False

    def __init__(self, data, register):
        self.data = data
        self.register = register
    def allow_read(self):
        if self.remember and self.validated:
            self.register.info("no pedir pin para lectura porque se recuerda")
            return True
        self.register.info("pedir pin para lectura")
        pin = input("* insert pin: ")
        if pin in self.data:
            self.register.info("pin correcto")
            if self.remember:
                self.validated = True
            return True
        else:
            self.register.warn("pin incorrecto")
            return False
    def allow_write(self):
        if self.remember and self.validated:
            self.register.info("no pedir pin para escritura porque se recuerda")
            return True
        self.register.info("pedir pin para escritura")
        pin = input("* insert pin: ")
        if pin in self.data:
            self.register.info("pin correcto")
            if self.remember:
                self.validated = True
            return True
        else:
            self.register.warn("pin incorrecto")
            return False
    def remember_pin(self):
        self.remember = True
        self.validated = False
    def forget_pin(self):
        self.remember = False
        self.validated = False
    
class auth_by_pin_simple(auth_by_pin):
    def __init__(self, data, register):
        super().__init__(data, register)
    def allow_read(self):
        self.register.info("no pedir pin para lectura por principio")
        return True

