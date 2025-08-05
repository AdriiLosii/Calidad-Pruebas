#!/usr/bin/env python
# encoding: utf-8

# Para cumplir r1:
def invertir(txt):
    return -1

# Para cumplir r2:
def invertir(txt):
    if txt == "": return None
    if len(txt) == 2: return txt[1]+txt[0]
    if len(txt) == 8: return txt[7]+txt[6]+txt[5]+txt[4]+txt[3]+txt[2]+txt[1]+txt[0]
    r = ""
    for i in range(len(txt)):
        r += txt[len(txt)-1-i]
    return r

# tests

# rq1: cadena vacía
def t_rq1():
    print("test rq1")
    if invertir("") == None:
        print("ok")
    else:
        print("not ok")

# rq2: caracter
def t_rq2():
    print("test rq2 t1")
    assert invertir("a") == "a"

    print("test rq2 t2")
    assert invertir("0") == "0"

    print("test rq2 t3")
    assert invertir("?") == "?"

    print("test rq2 t4")
    assert invertir("z") != "q"

def t_rq3():
    print("test rq3 t1")
    assert invertir("ab") == "ba"

    print("test rq3 t2")
    assert invertir("ba") == "ab"

    print("test rq3 t3")
    assert invertir("aa") == "aa"

    print("test rq3 t4")
    assert invertir("b2") == "2b"


if __name__ == "__main__":
    t_rq1()
    t_rq2()
    t_rq3()