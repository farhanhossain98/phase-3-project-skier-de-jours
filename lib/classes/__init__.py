import sqlite3

CONN = sqlite3.connect('lib/skijor.db')
CURSOR = CONN.cursor()  