import json
from urllib.request import urlopen

class remote_storage():
    def read(self):
        pass

class remote_storage_http(remote_storage):
    url = ""
    register = None
    def __init__(self, url, register):
        self.url = url
        self.register = register
    def read(self):
        self.register.info("acceder a '{}'".format(self.url))
        with urlopen(self.url) as f:
            try:
                return json.load(f)
            except:
                self.register.error("no se pudo :(")
                return None

# python3 -m http.server --bind 127.0.0.1 --directory /home/marcos/tmp/

