#!/usr/bin/python
# encoding: utf-8

import sys, datetime
from bcal_ls import local_storage_sqlite3
from bcal_rs import remote_storage_http

config = {
    #"base_de_datos": "/home/marcos/bcal.db",
    "base_de_datos": "/Users/marcos/Desktop/bcal0/bcal.db",
    "servidores": [
        "http://localhost:8000/test1.json",
        "http://localhost:8000/test2.json",
    ],
}

if __name__ == "__main__":
    print("** bcal v0")

    cmdline = sys.argv[1:]
    if len(cmdline) == 0: cmdline = ['check']
    cmd = cmdline[0].lower()
    if cmd == "help":
        print("ayuda:")
        print("  bcal list")
        print("  bcal [check]")
        print("  bcal add [--public] dd/mm \"msg\"")
        print("  bcal del n")
        print("  bcal update")
        print("  bcal server")

    elif cmd == "list":
        db = local_storage_sqlite3(config['base_de_datos'])
        for i in db.list():
            print(i)

    elif cmd == "check":
        n_meses = ["ene", "feb", "mar", "abr", "may", "jun",
            "jul", "ago", "sep", "oct", "nov", "dic"]
        n, m, z = False, False, False
        db = local_storage_sqlite3(config['base_de_datos'])
        for i in db.check():
            if i[0] == 0.0 and not n:
                print("\nhoy\n---")
                n = True
            elif i[0] == 1.0 and not m:
                print("\nmañana\n---")
                m = True
            else:
                if not z:
                    print("\npróximos días\n---")
                    z = True
            print("{}/{}\t{}".format(i[1], n_meses[i[2]-1], i[3]))

    elif cmd == "add":
        dia, mes, msj, p = -1, -1, "", False
        for i in cmdline[1:]:
            if i == '--public':
                p = True
                continue
            if dia == -1:
                f = i.split("/")
                if len(f)>1:
                    dia = int(f[0])
                    mes = int(f[1])
                else:
                    dia = int(f[0])
            else:
                if msj != "": msj += " "
                msj = msj + i
        if msj == "":
            msj = "?"
        # validar
        if dia<1 or dia>31:
            print("¡error! día fuera de rango: {}".format(dia))
        else:
            if mes<1 or mes>12:
                print("¡error! mes fuera de rango: {}".format(mes))
            else:
                try:
                    dd = datetime.datetime(datetime.datetime.now().year, mes, dia)
                    
                    # añadir
                    db = local_storage_sqlite3(config['base_de_datos'])
                    db.add(dia, mes, msj, p)

                except ValueError:
                    print("¡error! fecha fuera de rango: {}-{}-{} ".format(
                        datetime.datetime.now().year, mes, dia))

    elif cmd == "del":
        n = -1
        if len(cmdline)>1:
            n = int(cmdline[1])
        if n<0:
            print("¡error! identificador fuera de rango: {}".format(n))
        else:
            db = local_storage_sqlite3(config['base_de_datos'])
            db.delete(n)

    elif cmd == "update":
        dd = []
        for s in config['servidores']:
            print("** conectar con '{}'".format(s))
            a = remote_storage_http(s)
            b = a.read()
            if len(b)>0:
                dd = dd + b['data']
        db = local_storage_sqlite3(config['base_de_datos'])
        db.auth.remember_pin()
        cc = db.codes()
        for i in dd:
            if i[2] not in cc:
                db.add(i[3], i[4], i[5], i[1], i[2])
        db.auth.forget_pin()

    elif cmd == "server":
        print("comando server")

    else:
        print("¡error! comando no reconocido: {}".format(cmd))
