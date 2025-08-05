import time

class log_monitor():
    def info(self, msg):
        pass
    def warn(self, msg):
        pass
    def error(self, msg):
        pass

class log_monitor_file(log_monitor):
    name = ""
    fh = None
    
    def __init__(self, name):
        self.name = name
        self.fh = open(name, "a")
    def info(self, msg):
        self.write("[INFO]", msg)
    def warn(self, msg):
        self.write("[WARNING]", msg)
    def error(self, msg):
        self.write("[ERROR]", msg)
    def write(self, type, msg):
        try:
            self.fh.write("{} {} {}\n".format(type, str(time.time()), msg))
        except:
            print("¡error! imposible escribir en '{}'".format(self.name))
