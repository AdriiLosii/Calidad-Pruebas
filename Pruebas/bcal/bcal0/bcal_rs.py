import json
from urllib.request import urlopen

class remote_storage():
    def read(self):
        pass

class remote_storage_http(remote_storage):
    url = ""
    def __init__(self, url):
        self.url = url
    def read(self):
        with urlopen(self.url) as f:
            try:
                return json.load(f)
            except:
                return None

# python3 -m http.server --bind 127.0.0.1 --directory /home/marcos/tmp/

