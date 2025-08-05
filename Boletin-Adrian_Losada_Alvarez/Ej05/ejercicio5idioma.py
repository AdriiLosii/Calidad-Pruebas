import random

#
# módulo de idioma
#

class modulo_idioma():
    default_lang = ""
    dictionaries = {}
    def __init__(self, lang=[]):
        for i in lang:
            if i not in self.dictionaries.keys():
                j = self.load_dictionary_rules(i)
                self.dictionaries[i] = j
                if not self.default_lang:
                    self.default_lang = i
    #
    # simulación de cargar idioma
    #
    def load_dictionary_rules(self, lang):
        print("[debug] loading dictionary rules for lang '{}'".format(lang))
        if lang in ["es_ES", "en_US"]:
            return {"rules":{}, "vocabulary":{}}
        else:
            return self.download_dictionary_rules(lang)
    def download_dictionary_rules(self, lang):
        print("[debug] downloading dictionary rules for lang '{}'".format(lang))
        if random.random() >= 0.95: # probabilidad del 5%
            raise Exception("network error!")
        return {"rules":{}, "vocabulary":{}}
    #
    # simulación de revisar idioma
    #
    def check_word(self, txt, lang):
        if not lang: raise Exception("language not declared!")
        if lang not in self.dictionaries.keys(): raise Exception("language not loaded!")
        if random.random() >= 0.99: # probabilidad del 1%
            print("[debug] - - word '{}' not found for lang '{}'".format(txt, lang))
            return False
        else:
            return True
    def check_paragraph(self, data):
        print("[debug] - spellcheck paragraph")
        n, m = 0, 0
        if hasattr(data, "lang"):
            lang = data.lang
        else:
            lang = self.default_lang
        for p in data.txt.split():
            n += 1
            if not self.check_word(p, lang):
                m += 1
        return n, m
    def check_block(self, data):
        print("[debug] spellcheck block")
        n, m = 0, 0
        for t in data.texts:
            i, j = self.check_paragraph(t)
            n += i
            m += j
        return n, m  # número de palabras y de errores

