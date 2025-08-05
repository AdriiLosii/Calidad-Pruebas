class auth():
    def read_permission(self):
        pass
    def write_permission(self):
        pass

class auth_by_pin(auth):
    data = []
    remember = False
    validated = False

    def __init__(self, data):
        self.data = data
    def allow_read(self):
        if self.remember and self.validated:
            return True
        pin = input("* insert pin: ")
        if pin in self.data:
            if self.remember:
                self.validated = True
            return True
        else:
            return False
    def allow_write(self):
        if self.remember and self.validated:
            return True
        pin = input("* insert pin: ")
        if pin in self.data:
            if self.remember:
                self.validated = True
            return True
        else:
            return False
    def remember_pin(self):
        self.remember = True
        self.validated = False
    def forget_pin(self):
        self.remember = False
        self.validated = False
    
class auth_by_pin_simple(auth_by_pin):
    def __init__(self, data):
        super().__init__(data)
    def allow_read(self):
        return True
