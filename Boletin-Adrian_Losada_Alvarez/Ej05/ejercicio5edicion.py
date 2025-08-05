import random, copy

#
# módulo de edición
#

# componentes del bloque

class objeto_parrafo():
    txt = None
    def __init__(self, txt, lang=None):
        self.txt = txt
        if lang is not None: self.lang = lang

# componentes de la página

class objeto_imagen():
    filename, geometry = None, None
    def __init__(self, filename, geometry=(0, 0, -1, -1)):
        self.filename = filename
        self.geometry = geometry

class objeto_conector():
    geometry = None
    def __init__(self, geometry=(0, 0, -1, -1)):
        self.geometry = geometry

class objeto_bloque():
    texts = []
    geometry = None
    def __init__(self, texts=[], geometry=(0, 0, -1, -1)):
        self.texts = copy.deepcopy(texts)
        self.geometry = geometry
    def idiomas(self):
        l = []
        for t in self.texts:
            if hasattr(t, "lang"):
                if t.lang not in l:
                    l.append(t.lang)
        return l

# componentes del editor

class objeto_pagina():
    title = None
    blocks, images, arrows = [], [], []
    def __init__(self, title, blocks=[], images=[], arrows=[]):
        self.title = title
        if len(blocks): self.blocks = copy.deepcopy(blocks)
        if len(images): self.images = copy.deepcopy(images)
        if len(arrows): self.arrows = copy.deepcopy(arrows)
    #
    # bloques de la página
    #
    def crear_bloque(self, text_content, geometry):
        self.blocks.append(
            objeto_bloque(text_content, geometry)
        )
    def mover_bloque(self, m, n):
        b1 = self.blocks[:m] + self.blocks[m+1:]
        b2 = b1[:n] + [self.blocks[m]] + b1[n:]
        self.blocks = b2
    def eliminar_bloque(self, n):
        del(self.blocks[n])
    def idiomas(self):
        l = []
        for b in self.blocks:
            for i in b.idiomas():
                if i not in l:
                    l.append(i)
        return l
    #
    # otros elementos de la página
    #
    def crear_imagen(self, filename, geometry):
        ...
    def crear_flecha(self, geometry):
        ...

# código del módulo

class modulo_editor():
    config = {"default_lang":"en_US"}
    title = ""
    pages = []
    def __init__(self, title="", pages=[], config=None):
        if title: self.title = title
        if len(pages): self.pages = copy.deepcopy(pages)
        if config is not None: self.config = copy.deepcopy(config)
    def idioma_base(self, lang):
        self.config["default_lang"] = lang
    #
    # páginas del editor
    #
    def crear_pagina(self, title, blocks=[], images=[], arrows=[]):
        self.pages.append(
            objeto_pagina(title, blocks, images, arrows)
        )
    def mover_pagina(self, m, n):
        p1 = self.pages[:m] + self.pages[m+1:]
        p2 = p1[:n] + [self.pages[m]] + p1[n:]
        self.pages = p2
    def eliminar_pagina(self, n):
        del(self.pages[n])
    #
    # conexión con el gestor de idiomas
    #
    def idiomas(self):
        l = []
        if self.config["default_lang"]:
            l.append(self.config["default_lang"])
        for i in self.pages:
            for j in i.idiomas():
                if j not in l:
                    l.append(j)
        return l
    def revisar_pagina_texto(self, page, management_idiom_object):
        n, m = 0, 0
        for b in page.blocks:
            i, j = management_idiom_object.check_block(b)
            n += i
            m += j
        return n, m
    def revisar_bloque_texto(self, block, management_idiom_object):
        return management_idiom_object.check_block(block)


#
# debug
#

def debug_show_document_text_data(doc):
    print("DOCUMENT")
    print("TITLE '{}'".format(doc.title))
    n = 0
    for i in doc.pages:
        print("PAGE {} TITLE '{}'".format(n, i.title))
        m = 0
        for j in i.blocks:
            print("- BLOCK {}".format(m))
            if hasattr(j, "geometry"): print("  - GEOM {}".format(j.geometry))
            o = 0
            for k in j.texts:
                print("  - TEXT '{}'".format(o))
                print("     - TXT '{}'".format(k.txt))
                if hasattr(k, "lang"): print("     - LANG {}".format(k.lang))
                o += 1
            m += 1
        m = 0
        for j in i.images:
            print("- IMAGE {}".format(m))
            if hasattr(j, "geometry"): print("  - GEOM {}".format(j.geometry))
            print("  - FILE '{}'".format(j.filename))
            m += 1
        m = 0
        for j in i.arrows:
            print("- ARROW {}".format(m))
            if hasattr(j, "geometry"): print("  - GEOM {}".format(j.geometry))
            m += 1
        n += 1

test_config = {"default_lang":"es_ES"}
test_data = [
    objeto_pagina("primera página", [
        objeto_bloque(
            [objeto_parrafo("contenido del bloque de texto A")],
            (10, 10, 10, 10)
        ),
        objeto_bloque([
                objeto_parrafo("contenido del bloque de texto B"),
                objeto_parrafo("contenido del bloque de texto B"),
                objeto_parrafo("contenido del bloque de texto B")
            ],
            (30, 30, -1, -1)
        ),
        objeto_bloque(
            [objeto_parrafo("contenido del bloque de texto C")],
            (40, 40, -1, -1)
        ),
    ]),
    objeto_pagina("segunda página", [
        objeto_bloque([objeto_parrafo("<strong>text block</strong> content", lang="en_US")]),
        objeto_bloque([objeto_parrafo("<em>text block</em> content", lang="en_US")]),
        objeto_bloque([objeto_parrafo("<u>text block</u> content", lang="en_US")])
    ]),
    objeto_pagina("tercera página", images=[
        objeto_imagen("logo1.svg", (0, 0, -1, -1)),
        objeto_imagen("logo2.svg", (40, 40, 10, 10))
    ])
]

