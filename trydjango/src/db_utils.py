import sqlite3

class Database:
    def __init__(self, name):
        self._connection = sqlite3.connect(name)

    def commit(self):
        self._connection.commit()

    def execute(self, q, arg=None):
        cur = self._connection.cursor()
        if arg:
            cur.execute(q, arg)
        else:
            cur.execute(q)
        res = cur.fetchall()
        cur.close()
        return res