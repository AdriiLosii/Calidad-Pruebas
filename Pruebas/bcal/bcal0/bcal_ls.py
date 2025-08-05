import sqlite3
from bcal_auth import auth_by_pin, auth_by_pin_simple

class local_storage():
    def list(self):
        pass
    def check(self):
        pass
    def add(self, data):
        pass
    def delete(self, data):
        pass
    def update(self, data):
        pass

class local_storage_sqlite3(local_storage):
    db_name = None
    auth = None

    def __init__(self, name):
        self.db_name = name
        self.auth = auth_by_pin_simple(
            [i[0] for i in self._db_read("SELECT pin FROM u;")]
        )

    def _db_read(self, sql):
        c = sqlite3.connect(self.db_name)
        u = c.cursor()
        r = u.execute(sql).fetchall()
        return r

    def _db_write(self, sql, values=""):
        c = sqlite3.connect(self.db_name)
        u = c.cursor()
        r = u.execute(sql, values)
        c.commit()
        return

    def list(self):
        if self.auth.allow_read():
            return self._db_read("SELECT * FROM d ORDER BY id;")
        return None

    def codes(self):
        if self.auth.allow_read():
            r = self._db_read("SELECT c FROM d ORDER BY id;")
            return [i[0] for i in r]
        return None

    def check(self):
        if self.auth.allow_read():
            sql = '''with tmp as (
                select case
                when
                    date(printf("%d-%02d-%02d", strftime("%Y"), month, day)) >= date("now")
                then
                    julianday(date(printf("%d-%02d-%02d", strftime("%Y"), month, day))) - julianday(date("now"))
                else
                    julianday(date(printf("%d-%02d-%02d", strftime("%Y"), month, day), "+1 years")) - julianday(date("now"))
                end as dd, * from d)
                select dd, day, month, msg from tmp where dd <= 10 order by dd;'''
            return self._db_read(sql)
        return None

    def add(self, dia, mes, mensaje, publico=False, codigo=""):
        if self.auth.allow_write():
            if codigo:
                sql = "INSERT INTO d (p, c, day, month, msg) values (?, ?, ?, ?, ?);"
                self._db_write(sql, (publico, codigo, dia, mes, mensaje))
            else:
                sql = '''INSERT INTO d (p, c, day, month, msg) values (?, unixepoch()||'-'||hex(randomblob(4)), ?, ?, ?);'''
                self._db_write(sql, (publico, dia, mes, mensaje))
            return True
        return False

    def delete(self, n):
        if self.auth.allow_write():
            sql = "DELETE FROM d WHERE (id = ?);"
            self._db_write(sql, (n,))
            return True
        return False
