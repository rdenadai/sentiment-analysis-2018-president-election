import sqlite3
from contextlib import contextmanager


@contextmanager
def conn(fname):
    # conectando...
    conn = sqlite3.connect(fname)
    # definindo um cursor
    cursor = conn.cursor()
    yield cursor
    conn.close()
